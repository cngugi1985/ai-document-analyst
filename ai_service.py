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
Analyse this resume and provide a professional summary.

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
                - 5 improvement suggestions
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
        max_tokens=300
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
        max_tokens=800,
        temperature=0.3
    )

    return response.choices[0].message.content


def generate_career_roadmap(text):

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
        max_tokens=800,
        temperature=0.3
    )

    return response.choices[0].message.content


def generate_skill_gap_analysis(text):

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
        max_tokens=800,
        temperature=0.3
    )

    return response.choices[0].message.content


def generate_recommended_sectors(text):

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
        max_tokens=800,
        temperature=0.3
    )

    return response.choices[0].message.content


def generate_primary_sector(text):

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

    Return ONLY the most appropriate career sector.

    Examples:
    Software Engineering
    Data Analytics
    AI Operations
    Construction Technology
    Industrial Automation

    Return only the sector name.
    No explanation.
    No bullet points.
    No sentences.

    Resume:

    {text}
    """
            }
        ],
        max_tokens=20,
        temperature=0.3
    )

    return response.choices[0].message.content.strip()

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


def generate_existing_certifications(text):

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
                Extract all certifications, licenses,
                professional credentials and professional
                designations from this resume.

                Return only a bulleted list.

                Resume:

                {text}
                """
            }
        ],
        max_tokens=300,
        temperature=0.3
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
                Analyse this resume and generate a concise market intelligence dashboard.

Use the following sections exactly:

Primary Role
Related Industry
Salary Outlook
Market Demand
Growth Outlook
Recommended Certifications
High Value Skills To Add
Immediate Action Items

Use bullet points.

Formatting Rules:

- Use markdown headings and bullet points.
- Do not use code blocks.
- Do not use inline code.
- Do not use HTML tags.
- Keep formatting clean and simple.

Be concise.

Do not write long paragraphs.

Do not write introductions or conclusions.

Do not exceed 300 words.
                {text}
                """
            }
        ],
        max_tokens=800
    )

    return response.choices[0].message.content