import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def generate_summary(text):

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful document analyst."
            },
            {
                "role": "user",
                "content": f"Summarise this document:\n\n{text}"
            }
        ],
        max_tokens=400
    )

    return response.choices[0].message.content


def generate_improvements(text):

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a professional resume reviewer."
            },
            {
                "role": "user",
                "content": f"""
                Review this resume.

                Provide:
                - 5 improvement suggestions
                - Missing keywords
                - Ways to make achievements stronger

                Resume:

                {text}
                """
            }
        ],
        max_tokens=300
    )

    return response.choices[0].message.content

def generate_resume_score(text):

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are an expert resume reviewer."
            },
            {
                "role": "user",
                "content": f"""
                Review this resume.

Return exactly this format:

Score: X/100

Explanation:
2-3 sentences explaining the score.

Do not use markdown.
Do not use headings.
Do not use ### symbols.

                Resume:

                {text}
                """
            }
        ],
        max_tokens=150
    )

    return response.choices[0].message.content

def generate_career_paths(text):

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are an expert career strategist."
            },
            {
                "role": "user",
                "content": f"""
                Analyze this resume and provide:

                1. Top 3 recommended career paths
                2. Why the candidate is qualified
                3. Missing skills
                4. Estimated preparation time

                Keep the output concise and actionable.

                Resume:

                {text}
                """
            }
        ],
        max_tokens=500
    )

    return response.choices[0].message.content