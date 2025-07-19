# 💻 Laptop Security & Health Dashboard

A **full-stack web application** designed to provide a real-time security and health overview of your laptop.  
It features a **Python-based data collector**, a **Flask backend**, and a **modern, responsive frontend** for clear visualization.

---

## 🚀 Live Demo

- **Live Dashboard:** https://soarx.netlify.app/  
- **Backend API Host:** https://hello1235.pythonanywhere.com/


---

## 📸 Screenshots

**Light Mode**

![Light Mode Screenshot](assets/light_mode.png) <!-- Replace with your screenshot path -->

**Dark Mode**

![Dark Mode Screenshot](assets/dark_mode.png) <!-- Replace with your screenshot path -->

---

## ✅ Features

| Feature                  | Status | Description                                                    |
|--------------------------|--------|----------------------------------------------------------------|
| **Live Health Score**    | ✅     | An overall score calculated from real-time system metrics.     |
| **Real-time Resources**  | ✅     | Live monitoring of CPU, Memory, and Disk usage.                |
| **File Integrity Scan**  | ✅     | Hashes files from user directories to detect changes (simulated). |
| **High-Resource Processes** | ✅ | Lists top 10 most resource-intensive processes.                |
| **Active Network Connections** | ✅ | Shows active TCP/UDP connections.                              |
| **Detailed System Info** | ✅     | Displays OS, architecture, and version details.                |
| **Light & Dark Mode**    | ✅     | Modern UI with theme toggle that saves preference.             |

---

## 🗂️ System Architecture

┌─────────────────┐ ┌───────────────────────────────────┐ ┌───────────────────────────┐
│ │ │ │ │ │
│ Target Laptop │ │ PythonAnywhere Cloud Server │ │ Netlify Frontend │
│ (collector.py) │ │ (app.py) │ │ (index.html) │
│ │ │ │ │ │
└─────────────────┘ └───────────────────────────────────┘ └───────────────────────────┘
│ ▲ │ ▲
│ │ │ │
└────(1) Pushes JSON data────┘ └─────(2) Serves JSON────────┘
via POST via GET


- **Collector (`collector.py`)**: Runs on the laptop, collects system data, and pushes it to the backend.
- **Backend (`app.py`)**: Flask API hosted on PythonAnywhere. Receives and serves JSON data.
- **Frontend (`index.html`)**: Static site hosted on Netlify. Pulls data from backend and displays it.

---

## ⚙️ Technology Stack

- **Frontend:** HTML5, Tailwind CSS, Chart.js
- **Backend:** Python, Flask, Flask-CORS
- **Collector:** Python, psutil, requests
- **Deployment:** PythonAnywhere (Backend), Netlify (Frontend)

---

## 🛠️ How to Run Locally

1️⃣ **Clone the repository:**

```bash
git clone [YOUR GITHUB REPO URL]
cd LaptopSecurityDashboard
# Navigate to the backend folder
cd backend

# Create and activate a virtual environment
python -m venv venv

# On Windows
.\venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate

# Install dependencies
pip install Flask Flask-Cors requests psutil
python backend/app.py
# Open a new terminal, activate the venv if needed
python collector/collector.py
