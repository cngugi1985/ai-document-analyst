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
def extract_current_role(text):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": f"""Analyze the resume and identify the candidate's most recent or current job title.

Rules:
- Return only one title.
- Use the actual title from the resume.
- Do not rewrite the title.
- Do not infer a higher title.
- Do not suggest an alternative title.
- Return only the exact role title.

Resume:
{text}
"""
            }
        ],
        max_tokens=100,
        temperature=0
    )

    return response.choices[0].message.content

def classify_role_level(role):

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": f"""
Classify this job title into ONE salary band.

Valid salary bands:

Analyst
Senior Analyst
Engineer
Senior Engineer
Manager
Senior Manager
Director
Vice President

Rules:
- Return only one salary band.
- No explanation.
- No punctuation.
- No extra text.

Job Title:

{role}
"""
            }
        ],
        max_tokens=20,
        temperature=0
    )

    return response.choices[0].message.content.strip()


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
                - Use 'you' and 'your'
                - Never use the candidate's name
                - Never refer to the user in third person

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
- Maximum 3 bullet points
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
- Recommend exactly 2 certifications.
- Choose the 2 certifications with the highest practical value for the candidate's current role and experience.
- Certifications only.
- Do not recommend job titles.
- Do not recommend career paths.
- Do not include explanations.
- Do not include numbering.
- Do not include bullets.
- One certification per line.
Press Enter after each certification.
Return exactly two separate lines.
- Return exactly 2 lines and nothing else.

Example:

Certified Information Systems Security Professional (CISSP)

Certified Information Security Manager (CISM)

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



