import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

SYSTEM_PROMPT = """
You are an expert career strategist and career coach.

Focus on helping users identify:
- Career paths
- Skill development opportunities
- Valuable certifications
- Career progression opportunities

Provide concise, actionable recommendations.
"""


def generate_summary(text):

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": f"""
Analyse this resume. 
Requirements:
- Use 'you' and 'your'
- Never use the candidate's name
- Never refer to the user in third person
- Write like a career coach speaking directly to the user
- Highlight strengths, experience, achievements and growth opportunities

Resume:

{text}
"""
            }
        ],
        max_tokens=800,
        temperature=0.3
    )

    return response.choices[0].message.content


def generate_improvements(text):

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": f"""
                Review this resume.

                Provide:
                - 3 improvement suggestions
                - Missing keywords
                - Ways to make achievements stronger

                Resume:

                {text}
                """
            }
        ],
        max_tokens=800,
        temperature=0.3
    )

    return response.choices[0].message.content


def generate_resume_score(text):

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": f"""
                Review this resume.

Return ONLY a resume score.

Format:
65/100

No explanation.
No recommendations.
No extra text.

                Resume:

                {text}
                """
            }
        ],
        max_tokens=800
    )

    return response.choices[0].message.content


def generate_career_paths(text):

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": f"""
                Analyze this resume and provide:

                Analyze this resume.

Return ONLY:

Top 3 Career Matches

Rules:
- Maximum 3 roles
- Show logical progression from nearest role to long-term role
- Use this format:

Role 1
↓
Role 2
↓
Role 3

- No numbering
- No explanations
Resume:

{text}
                """
            }
        ],
        max_tokens=800,
        temperature=0.3
    )

    return response.choices[0].message.content







def generate_skills_to_develop(text):

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": f"""
                Analyze this resume.

Return ONLY:

Top Skills To Add

Rules:
- Maximum 5 bullet points
- One line per bullet
- No current strengths
- No explanations
- No action steps
- No introductions
- No conclusions
- Maximum 50 words total

Resume:

{text}
                """
            }
        ],
        max_tokens=800,
        temperature=0.3
    )

    return response.choices[0].message.content







def generate_recommended_certifications(text):

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": f"""
                Based on this resume, Return ONLY certification recommendations.

Rules:
- Maximum 3 certifications
- Always provide the full certification name followed by the acronym in parentheses
- One certification per line
- No descriptions
- No bullet explanations
- No introductions or conclusions

Example:

Certified Information Systems Security Professional (CISSP)

Certified Information Security Manager (CISM)

CompTIA Cybersecurity Analyst (CySA+)

Resume:

{text}
                """
            }
        ],
        max_tokens=200
    )

    return response.choices[0].message.content


def generate_next_career_move(text):

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": f"""
Analyze this resume.

Return ONLY:

Next Best Move:
[role]

Actions:
• action 1
• action 2
• action 3

Rules:
- Recommend only ONE role
- Maximum 3 actions
- No explanations
- No introductions
- No conclusions
- No extra commentary
- Maximum 30 words total

Resume:

{text}
"""
            }
        ],
        max_tokens=100,
        temperature=0.3
    )

    return response.choices[0].message.content


