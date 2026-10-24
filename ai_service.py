import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

SYSTEM_PROMPT = """
You are an expert resume reviewer and career coach.

Address the user directly using 'you' and 'your'.

Never refer to the candidate by name.

Always write in second person.

Provide specific, actionable recommendations.

Avoid generic corporate buzzwords.
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

Top Career Matches

Rules:
- Maximum 3 career matches
- One bullet per role
- No explanations
- No preparation time
- No qualification analysis
- No additional commentary

Resume:

{text}
                """
            }
        ],
        max_tokens=800,
        temperature=0.3
    )

    return response.choices[0].message.content




def generate_career_blindspots(text):

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

Biggest Career Gaps

Rules:
- Maximum 5 bullet points
- One line per bullet
- No introductions
- No explanations
- No recommendations
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


def generate_Skills_To_Develop(text):

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


def generate_action_plan(text):

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
                Based on this resume:

                Create a practical 60-day action plan.

                Provide:
                1. Top 3 actions
                2. Expected career impact

                Keep it concise.

                Resume:

                {text}
                """
            }
        ],
        max_tokens=800,
        temperature=0.3
    )

    return response.choices[0].message.content


def generate_primary_role(text):

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

                Return ONLY the most suitable job role.

                Examples:

                Software Engineer
                Data Analyst
                Technical Program Manager
                Construction Project Manager
                Automation Engineer

                Return only the role.

                No explanation.
                No bullets.
                No sentences.

                Resume:

                {text}
                """
            }
        ],
        max_tokens=20
    )

    return response.choices[0].message.content.strip()



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
                Based on this resume, recommend the top 5
                certifications that would most improve career
                prospects.

                Return only certification names.

                One certification per line.

                No explanations.

                Resume:

                {text}
                """
            }
        ],
        max_tokens=200
    )

    return response.choices[0].message.content

def generate_market_intelligence(text):

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
                Analyse this resume and Generate a concise career market dashboard.

Include only:

Salary Outlook
Market Demand
Growth Outlook
High Value Skills To Add

Formatting Rules:

- No paragraphs.
- No introductions.
- No conclusions.
- No # symbols.
- No markdown headings.
- Keep responses concise.
- Use bullet points only for certifications and skills.
- Maximum 100 words.
- Do not use code formatting.
- Do not use backticks.
- Do not use HTML.
- Do not use markdown code blocks.

                {text}
                """
            }
        ],
        max_tokens=800
    )

    return response.choices[0].message.content

