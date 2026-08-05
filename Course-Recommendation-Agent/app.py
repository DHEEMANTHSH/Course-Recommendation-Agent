"""
app.py
Flask backend for the AI Course Recommendation Agent.
"""

import os
from flask import Flask, jsonify, request, send_from_directory
from recommendation import get_recommendations, load_json

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/api/students', methods=['GET'])
def get_students():
    students = load_json('students.json')
    return jsonify(students)

@app.route('/api/courses', methods=['GET'])
def get_courses():
    courses = load_json('courses.json')
    return jsonify(courses)

@app.route('/api/recommend', methods=['POST'])
def recommend_courses():
    data = request.get_json()
    student_id = data.get('student_id')

    if not student_id:
        return jsonify({"error": "student_id is required"}), 400

    try:
        recommendations = get_recommendations(student_id)
        return jsonify(recommendations)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port)