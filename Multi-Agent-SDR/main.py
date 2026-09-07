from agents import (
    lead_generation_agent,
    lead_qualification_agent,
    email_agent
)


company_profile = """
Our company provides an AI-powered customer support
platform for SaaS companies.

The platform helps companies automate customer questions,
reduce support workload, and improve response times.

Ideal customers:
- SaaS companies
- 100+ employees
- Growing customer support teams
- Technology companies
"""


# ==========================================
# AGENT 1
# ==========================================

print("=" * 60)
print("AGENT 1: LEAD GENERATION")
print("=" * 60)

leads = lead_generation_agent(company_profile)

print(leads)


# ==========================================
# AGENT 2
# ==========================================

print("\n")
print("=" * 60)
print("AGENT 2: LEAD QUALIFICATION")
print("=" * 60)

qualification = lead_qualification_agent(leads)

print(qualification)


# ==========================================
# AGENT 3
# ==========================================

print("\n")
print("=" * 60)
print("AGENT 3: EMAIL GENERATION")
print("=" * 60)

email = email_agent(
    leads,
    qualification
)

print(email)
