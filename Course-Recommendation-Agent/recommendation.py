"""
recommendation.py
Handles data loading and calls the Google GenAI SDK for recommendations.
"""

import os
import json
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompt import SYSTEM_INSTRUCTION, build_recommendation_prompt

# Load environment variables from .env file
load_dotenv()

def load_json(filepath):
    if not os.path.exists(filepath):
        return []
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_recommendations(student_id: str):
    # Load data files
    base_dir = os.path.dirname(os.path.abspath(__file__))
    students_path = os.path.join(base_dir, 'students.json')
    courses_path = os.path.join(base_dir, 'courses.json')

    students = load_json(students_path)
    courses = load_json(courses_path)

    # Find target student
    student = next((s for s in students if s['student_id'] == student_id), None)
    if not student:
        raise ValueError(f"Student with ID '{student_id}' not found.")

    # Initialize Gemini Client explicitly with the environment variable
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    prompt = build_recommendation_prompt(student, courses)

    # Call Gemini 3.5 Flash with structured reasoning
    response = client.models.generate_content(
        model='gemini-3.5-flash',
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_INSTRUCTION,
            temperature=0.3,
            response_mime_type="application/json"
        ),
    )

    try:
        result_json = json.loads(response.text)
        return result_json
    except json.JSONDecodeError:
        # Fallback if raw text needs cleaning
        return {"raw_response": response.text}