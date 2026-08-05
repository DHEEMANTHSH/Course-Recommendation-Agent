"""
prompt.py
System instructions and structured prompts for the Course Recommendation Agent.
"""

SYSTEM_INSTRUCTION = """
You are an expert AI Academic Advisor and Course Recommendation Agent. 
Your goal is to analyze a student's profile (completed courses, current skills, and career goals) 
against a provided catalog of available courses. 

Provide personalized, logical, and actionable course recommendations. Ensure that:
1. Prerequisites for recommended courses are satisfied by the student's completed courses or concurrent learning.
2. Recommendations directly align with the student's stated career goals.
3. Clear explanations are given for *why* each course is recommended.
"""

def build_recommendation_prompt(student_data: dict, courses_data: list) -> str:
    import json
    return f"""
Please analyze the following student profile and available course catalog, then generate personalized course recommendations.

### Student Profile:
{json.dumps(student_data, indent=2)}

### Available Course Catalog:
{json.dumps(courses_data, indent=2)}

### Output Requirements:
Return a valid JSON object matching this exact structure (no markdown formatting outside the JSON, or wrap it cleanly):
{{
  "student_id": "string",
  "student_name": "string",
  "readiness_summary": "string analyzing student's current standing",
  "recommended_courses": [
    {{
      "course_id": "string",
      "title": "string",
      "priority": "High / Medium / Low",
      "reason": "Detailed explanation connecting course to goals and skills"
    }}
  ],
  "estimated_time_to_goal": "string"
}}
"""