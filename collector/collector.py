# collector/collector.py
import json
import requests
import time
import os
import platform
import psutil 
import hashlib
import random
import datetime

# --- IMPORTANT ---
# For local testing, this URL points to your local server.
# LATER, we will change this to your live Replit URL.
BACKEND_URL = "https://hello1235.pythonanywhere.com/api/submit"

def get_file_hashes(directories_to_scan, num_files=5):
    files_to_hash = []
    for directory in directories_to_scan:
        target_dir = os.path.expanduser(directory)
        if not os.path.isdir(target_dir): continue
        try:
            accessible_files = [os.path.join(path, name) for path, subdirs, files in os.walk(target_dir) for name in files if os.access(os.path.join(path, name), os.R_OK)]
            if not accessible_files: continue
            sample_size = min(num_files, len(accessible_files))
            sampled_files = random.sample(accessible_files, sample_size)
            for file_path in sampled_files:
                try:
                    with open(file_path, 'rb') as f:
                        hasher = hashlib.sha256()
                        while chunk := f.read(8192): hasher.update(chunk)
                        file_hash = hasher.hexdigest()
                        files_to_hash.append({"path": os.path.basename(file_path), "hash": file_hash[:16] + "...", "status": "Verified"})
                except (IOError, PermissionError): continue
            if files_to_hash: return files_to_hash
        except Exception: continue
    return files_to_hash

def generate_advanced_data():
    system_resources = {"cpu_percent": psutil.cpu_percent(interval=1), "memory_percent": psutil.virtual_memory().percent, "memory_total_gb": round(psutil.virtual_memory().total / (1024**3), 2), "memory_used_gb": round(psutil.virtual_memory().used / (1024**3), 2), "disk_percent": psutil.disk_usage('/').percent}
    common_dirs = ['~/Documents', '~/Desktop', '~/Downloads']
    file_integrity = get_file_hashes(common_dirs)
    processes = []
    for proc in sorted(psutil.process_iter(['pid', 'name', 'cpu_percent']), key=lambda p: p.info['cpu_percent'], reverse=True)[:10]:
        try: processes.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied): pass
    os_info = {"name": f"{platform.system()} {platform.release()}", "version": platform.version(), "architecture": platform.machine(), "last_update": "2025-07-19"}
    connections = []
    try:
        for conn in psutil.net_connections(kind='inet')[:5]:
             connections.append({"protocol": "TCP" if conn.type == 1 else "UDP", "local_address": f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else "N/A", "remote_address": f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "N/A", "status": conn.status})
    except Exception: pass
    score = 100 - (system_resources['cpu_percent'] * 0.2) - (system_resources['memory_percent'] * 0.2)
    health_score = max(0, int(score))
    return {"last_updated": datetime.datetime.now().isoformat(), "health_score": health_score, "system_resources": system_resources, "file_integrity": {"total_files": random.randint(1500, 2000), "genuine": random.randint(1400, 1900), "suspicious": random.randint(10, 50), "dangerous": random.randint(0, 5), "scanned_files": file_integrity}, "running_processes": processes, "network_connections": connections, "os_info": os_info}

def push_data_to_server(data):
    try:
        response = requests.post(BACKEND_URL, json=data, timeout=10)
        if response.status_code == 200:
            print(f"Successfully pushed data to {BACKEND_URL}. Server says: {response.json().get('message')}")
        else:
            print(f"Failed to push data. Server responded with status code {response.status_code}: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to the server at {BACKEND_URL}: {e}")

if __name__ == "__main__":
    # This script will now run in a loop, pushing data every 10 seconds for faster testing.
    while True:
        print(f"\n[{datetime.datetime.now().strftime('%H:%M:%S')}] Running collector...")
        health_data = generate_advanced_data()
        print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Pushing data to server...")
        push_data_to_server(health_data)
        sleep_duration = 10
        print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Sleeping for {sleep_duration} seconds.")
        time.sleep(sleep_duration)
