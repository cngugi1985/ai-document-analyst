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

def generate_career_roadmap(text):

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

                1. Current Career Positioning
                2. Best Next Role (0-12 months)
                3. Recommended 2-Year Goal
                4. Recommended 5-Year Goal
                5. Skills Needed
                6. Learning Order
                7. Biggest Career Accelerator

                Keep recommendations realistic,
                concise and actionable.

                Resume:

                {text}
                """
            }
        ],
        max_tokens=700
    )

    return response.choices[0].message.content

def generate_career_blindspots(text):

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are an expert executive career coach."
            },
            {
                "role": "user",
                "content": f"""
                Analyze this resume.

                Identify:

                1. Hidden strengths
                2. Undersold skills
                3. Career opportunities the candidate
                   may be overlooking
                4. Why these opportunities are valuable

                Be specific and actionable.

                Resume:

                {text}
                """
            }
        ],
        max_tokens=600
    )

    return response.choices[0].message.content

def generate_skill_gap_analysis(text):

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
                Analyze this resume and identify:

                1. Current strengths
                2. Skill gaps
                3. Highest-impact skills to learn
                4. Which skills will produce the biggest career growth
                5. Recommended learning order

                Resume:

                {text}
                """
            }
        ],
        max_tokens=700
    )

    return response.choices[0].message.content
def generate_action_plan(text):

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are an expert career coach."
            },
            {
                "role": "user",
                "content": f"""
                Based on this resume:

                Create a practical 30-day action plan.

                Provide:
                1. Top 5 actions
                2. Skill priority
                3. Expected career impact

                Keep it concise.

                Resume:

                {text}
                """
            }
        ],
        max_tokens=500
    )

    return response.choices[0].message.content

def generate_recommended_sectors(text):

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a labour market and career strategy expert."
            },
            {
                "role": "user",
                "content": f"""
                Analyze this resume.

                Recommend:

                1. Top 5 industries/sectors
                2. Why the candidate fits them
                3. Typical roles available
                4. Career growth potential

                Keep the response concise.

                Resume:

                {text}
                """
            }
        ],
        max_tokens=600
    )

    return response.choices[0].message.content

def generate_primary_sector(text):

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": """
                You are a labour market expert.

                Return ONLY ONE sector.

                Allowed responses:

                Industrial Automation
                Advanced Manufacturing
                Construction Technology
                Infrastructure Technology
                AI Operations

                Return only the sector name.
                """
            },
            {
                "role": "user",
                "content": text
            }
        ],
        max_tokens=20
    )

    return response.choices[0].message.content.strip()