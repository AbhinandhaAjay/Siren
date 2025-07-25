
# siren
#https://github.com/user-attachments/assets/c607d049-e1d8-4608-b6ca-b21a7246035d
**siren** is an AI-powered real-time safety monitoring system that detects road accidents using CCTV footage, analyzes vehicle and speed data, summarizes incidents using GenAI, and alerts nearby emergency responders — reducing response time and improving public safety.

---

## Features

-  **Accident Detection**  
  Detects road accidents in real-time from CCTV feeds using YOLOv8.

-  **Vehicle & Speed Analysis**  
  Identifies vehicle types, calculates estimated speed, and assesses accident severity.

-  **Incident Summarization**  
  Uses Gemini (Google GenAI) API to convert raw detection data into clear, human-readable reports.

-  **Automated Emergency Alerts**  
  Sends alerts to nearby hospitals and police stations, improving coordination and response efficiency.

-  **Django Dashboard**  
  Provides an intuitive interface for hospitals and police to view incidents and manage responses.

---

## Tech Stack

| Layer            | Technologies                               |
|------------------|--------------------------------------------|
| **Frontend**     | React.js, Tailwind.css                     |
| **Backend APIs** | Flask (YOLO detection), FastAPI            |
| **AI/ML**        | YOLOv8, OpenCV                             |
| **NLP/GenAI**    | Gemini API (Google GenAI)                  |
| **Dashboard**    | Django                                     |

---

## Project Structure

```

siren/
├── flask_engine/             # Flask server running YOLOv8 model & React web interface
├── siren-backend/                  # Django dashboard and database
├── siren-frontend/        
├── vdos/
└── README.md

````

---

##  How to Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/AbhinandhaAjay/Siren.git
cd siren
````

### 2. Run YOLO Backend (Flask)

```bash
cd flask_engine
pip install -r requirements.txt
python app.py
```

### 3. Start the React Frontend

```bash
cd flask_engine/frontend
npm install
npm start
```
### 4. Start the Django Dashboard Backend
```bash
cd siren-backend
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### 5. Start Django Dashboard

```bash
cd siren-frontend
python manage.py runserver
```

---
