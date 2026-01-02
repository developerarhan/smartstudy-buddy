📘 SmartStudy Buddy

AI-Powered Personalized Study Planner

SmartStudy Buddy is a full-stack web application that generates personalized, day-wise and hour-wise study plans using AI.
It helps students plan their learning efficiently based on subject, available study hours, and total days.

🌟 Features

  - 🧠 AI-Generated Study Plans
      - Day-wise breakdown
      - Hour-wise subtopics per day
  - 🎯 Personalized input (subject, hours/day, total days)
  - ⚡ Fast & responsive UI (React + Vite)
  - 🔥 Modern UI/UX design
  - 🌐 REST API backend
  - ☁️ Fully deployed (Frontend + Backend)

## 📂 Repository Structure
  This repository uses multiple branches:
  
  - **main** → Project documentation
  - **frontend** → React frontend application
  - **backend** → Django REST API backend
 
  Please switch branches to view the respective code.

🛠 Tech Stack

  Frontend
    - React (Vite)
    - JavaScript (ES6+)
    - CSS (Custom modern UI)
    - Fetch API
    
  Backend
    - Django 
    - Django REST Framework
    - Groq LLM API
    - Python
    - SQLite (can be upgraded)
    
  Deployment
   - Frontend: Render (Static Site)
   - Backend: Render (Web Service)

🚀 Live Demo
  - Frontend:
    👉 https://smartstudy-frontend.onrender.com
  - Backend API Health:
    👉 https://smartstudy-backend-1okw.onrender.com/api/health

📂 Project Structure

smartstudy-buddy/
│
├── backend/
│   ├── api/
│   │   ├── ai_utils.py
│   │   ├── views.py
│   │   ├── serializers.py
│   ├── smartstudy/
│   ├── manage.py
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── services/
│   │   ├── styles/
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── package.json
│   └── vite.config.js
│
└── README.md

⚙️ Environment Variables
  Create a .env file in the backend directory:
      GROQ_API_KEY=your_groq_api_key_here

🧪 Local Setup

  - 1️⃣ Clone the Repository
    - git clone https://github.com/developerarhan/smartstudy-buddy.git
    - cd smartstudy-buddy

  - 2️⃣ Backend Setup
    - cd backend
    - python -m venv study_env 
    - study_env\Scripts\activate   # Windows
    - pip install -r requirements.txt
    - python manage.py migrate
    - python manage.py runserver
  - Backend will run at:
    http://127.0.0.1:8000

  - 3️⃣ Frontend Setup
    - cd frontend
    - npm install
    - npm run dev
  - Frontend will run at:
    http://localhost:5173

🔌 API Endpoints

  Generate Study Plan
    - POST /api/study-plan/
    
  Request Body
    {
      "subject": "Machine Learning",
      "hours_per_day": 3,
      "days": 7
    }
    
  Response
    {
      "success": true,
      "data": {
        "subject": "Machine Learning",
        "total_days": 7,
        "plan": [
          {
            "day": 1,
            "topic": "Introduction to ML",
            "hours": 3,
            "blocks": [
              { "hour": 1, "task": "Basics of ML" },
              { "hour": 2, "task": "Types of ML" },
              { "hour": 3, "task": "Revision & Practice" }
            ]
          }
        ]
      }
    }

💡 Future Enhancements

  - 🔐 User authentication (JWT)
  - 💾 Save & revisit study plans
  - 📊 Progress tracking
  - 📱 Mobile responsive improvements
  - 🌍 Multi-language support

👨‍💻 Author

  Arhan Khan
  - B.Tech (AIML)
  - Full-Stack Developer
  - Passionate about AI & Web Development
  - 🔗 GitHub: https://github.com/developerarhan
  
  MD Hammad
  - B.Tech (AIML)
  - Full-Stack Developer
  - Collaborator on SmartStudy Buddy
  - 🔗 GitHub: https://github.com/ZeroxxG
  
  📌 Both contributors worked on the same branch and same deployed domain

📄 License
This project is licensed under the MIT License.
You’re free to use, modify, and distribute it.

⭐ Support
If you like this project:
- ⭐ Star the repo
- 🛠 Fork and build on it
- 📢 Share with others
