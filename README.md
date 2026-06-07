# AI Habit Coach

A modern, AI-powered habit tracking application designed to help users build lasting routines through personalized coaching and intelligent insights.

## 🚀 Overview

AI Habit Coach combines traditional habit tracking with generative AI to provide a more interactive and supportive experience. Instead of just checking boxes, users can chat with an AI coach, receive weekly performance insights, and integrate their habits with their digital lives.

## ✨ Key Features

-   **Intelligent Habit Tracking:** Easy-to-use dashboard for logging daily, weekly, and monthly habits.
-   **AI Coach:** An interactive chat interface (powered by Anthropic Claude) that provides motivation, advice, and habit-building strategies.
-   **Progress Visualization:** Visual charts and streak tracking to monitor long-term consistency.
-   **Voice Commands:** Hands-free habit logging and interaction.
-   **Calendar Integration:** Sync habits with Google Calendar for seamless reminders.
-   **Weekly Insights:** Automated reports analyzing habit patterns and providing actionable feedback.

## 🛠 Tech Stack

### Frontend
-   **React 18** (TypeScript)
-   **Vite** (Build tool)
-   **Tailwind CSS** (Utility-first styling)
-   **Zustand** (State management)
-   **Lucide React** (Iconography)

### Backend (Upcoming)
-   **FastAPI** (Python web framework)
-   **PostgreSQL** (Database)
-   **SQLAlchemy** (ORM)
-   **Pydantic** (Data validation)

### AI
-   **Anthropic Claude API** (LLM for coaching and analysis)

## 📂 Project Structure

```text
ai-habit-coach/
├── ai/                 # AI Agent logic and prompts
├── backend/            # FastAPI application (Python)
│   ├── app/            # Main application logic
│   └── requirements.txt
├── frontend/           # React/Vite application (TypeScript)
│   ├── src/            # Components, hooks, and pages
│   └── package.json
├── infra/              # Docker, Nginx, and CI/CD configurations
├── tests/              # Unit, integration, and E2E tests
├── docs/               # Detailed technical documentation
├── .env.example        # Environment variables template
└── docker-compose.yml  # Local development orchestration
```

## 🚦 Getting Started

### Prerequisites
-   Node.js (v18+)
-   Python 3.10+
-   npm or yarn

### Frontend Setup
1.  Navigate to the `frontend` directory:
    ```bash
    cd frontend
    ```
2.  Install dependencies:
    ```bash
    npm install
    ```
3.  Start the development server:
    ```bash
    npm run dev
    ```
4.  Open `http://localhost:3000` in your browser.

### Backend Setup (Initial)
1.  Navigate to the `backend` directory:
    ```bash
    cd backend
    ```
2.  Create a virtual environment:
    ```bash
    python -m venv venv
    ```
3.  Activate the environment and install requirements:
    ```bash
    # Windows
    .\venv\Scripts\activate
    pip install -r requirements.txt
    ```

## 📄 License

This project is licensed under the MIT License.
