# 🎵 Hit Predictor

A simple machine learning project that predicts the popularity of a song based on audio features like danceability, valence and energy. Built with **FastAPI**, **React**, **Tailwind CSS**, **Docker** and **scikit-learn**.

---

## 🚀 Features

- 🔢 Predict song popularity based on audio features
- 🎛️ Web UI built with React + Tailwind CSS
- 🧠 Trained regression model with scikit-learn
- 🐳 Fully containerized with Docker + Docker Compose
- 🌐 Ready to deploy or run locally

---

## 🗂️ Project Structure

HitPredictor/
├── backend/ # FastAPI + ML model (.pkl)
│ ├── api/ # FastAPI routes
│ ├── model/ # train_model.py + saved model
│ └── requirements.txt
├── frontend/ # React + Vite + Tailwind
│ ├── src/
│ └── package.json
├── .env # Global environment config
├── docker-compose.yml # Multi-service orchestration
├── README.md # This file

---

## ⚙️ Getting Started

### 🔧 Prerequisites

- Docker + Docker Compose
- Python 3.10+ (for local training)
- Node.js 18+ (if running frontend locally)

---

### 💻 Local Dev (without Docker)

1. **Train model**
   ```bash
   cd backend
   python -m venv .venv
   .venv\Scripts\activate  # or source .venv/bin/activate
   pip install -r requirements.txt
   python model/train_model.py
Run backend

uvicorn api.main:app --reload
Run frontend

cd frontend
npm install
npm run dev
🐳 Run with Docker
Build and start containers:

docker compose up --build
App will be available at:

Frontend: http://localhost:5173

Backend: http://localhost:8000/docs

📦 API Endpoint
POST /predict
Input JSON:

{
  "danceability": 0.75,
  "valence": 0.9,
  "energy": 0.85
}
Response:

{
  "predicted_popularity": 81.6
}
📚 TODOs & Ideas
🎶 Integrate Spotify API to auto-fill features

📈 Train model on real dataset (Spotify Top 200)

🎨 Add chart comparison (radar or bar)

🛡️ Add validation, auth, logging

🌍 Deploy to Azure or Railway