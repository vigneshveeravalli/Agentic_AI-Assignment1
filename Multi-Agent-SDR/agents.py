import json
import requests


MODEL = "llama3.2"


def ask_llm(prompt):

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        }
    )

    response.raise_for_status()

    return response.json()["response"]


# ==========================================
# AGENT 1: LEAD GENERATION
# ==========================================

def lead_generation_agent(company_profile):

    prompt = f"""
You are a Lead Generation Agent.

Your job is to identify the ideal type of business
prospects for a company.

Company profile:
{company_profile}

Generate 3 fictional example leads that match
the ideal customer profile.

For each lead provide:
- Name
- Company
- Role
- Industry
- Company size
- Business problem

Do not provide real personal contact information.
"""

    return ask_llm(prompt)


# ==========================================
# AGENT 2: LEAD QUALIFICATION
# ==========================================

def lead_qualification_agent(lead):

    prompt = f"""
You are a Lead Qualification Agent.

Evaluate the following lead:

{lead}

Use these criteria:

1. Industry relevance
2. Job role relevance
3. Company size
4. Likelihood of needing the product

Classify the lead as:

HIGH
MEDIUM
LOW

Then explain the reason briefly.

Return:

Lead:
Qualification:
Score:
Reason:
"""

    return ask_llm(prompt)


# ==========================================
# AGENT 3: EMAIL GENERATION
# ==========================================

def email_agent(lead, qualification):

    prompt = f"""
You are an Email Writing Agent.

Create a short professional B2B outreach email.

Lead:
{lead}

Qualification:
{qualification}

Requirements:
- Write a personalized but professional email.
- Mention the recipient's company.
- Explain one relevant business benefit.
- Use a simple call to action.
- Do not make unsupported claims.
- Do not invent personal information.
- Keep it under 120 words.
- Return ONLY the email.

Subject:
...

Body:
...
"""

    return ask_llm(prompt)