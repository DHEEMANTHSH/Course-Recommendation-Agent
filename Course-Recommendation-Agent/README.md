# AI Course Recommendation Agent

An intelligent, full-stack academic advising agent powered by **Google Gemini** (`gemini-2.5-flash`), Flask, and a modern web frontend. This application analyzes student profiles—including completed courses, current skills, and career goals—against a comprehensive course catalog to generate tailored, prioritized learning paths.

## 🚀 Features

- **AI-Powered Analysis:** Leverages Gemini to evaluate student readiness and map out optimized learning trajectories.
- **Structured JSON Outputs:** Ensures deterministic, reliable responses using Pydantic/Gemini structured generation configurations.
- **Interactive Dashboard:** Clean, responsive frontend built with vanilla JavaScript and modern CSS.
- **Production-Ready Structure:** Separates backend routing, AI prompting logic, and static assets cleanly.

---

## 📁 Project Structure

```text
Course-Recommendation-Agent/
│
├── app.py                 # Flask backend server
├── recommendation.py      # Core Gemini API integration & logic
├── prompt.py              # System instructions and prompt templates
├── courses.json           # Course database catalog
├── students.json          # Student profile records
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
├── sample_output/
│   └── output.json        # Sample JSON response from the agent
├── index.html             # Frontend dashboard UI
├── style.css              # Dashboard styles
└── script.js              # Frontend interactivity & API fetching