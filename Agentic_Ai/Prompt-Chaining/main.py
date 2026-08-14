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


# ------------------------------------------------
# Read document
# ------------------------------------------------

with open("document.txt", "r", encoding="utf-8") as file:
    document = file.read()


# ------------------------------------------------
# STEP 1: Extract key information
# ------------------------------------------------

prompt1 = f"""
Read the following document.

Extract the most important facts, ideas, problems,
and conclusions.

Do not write a summary yet.

Document:
{document}
"""

key_information = ask_llm(prompt1)

print("\n===== STEP 1: KEY INFORMATION =====")
print(key_information)


# ------------------------------------------------
# STEP 2: Organize information
# ------------------------------------------------

prompt2 = f"""
Organize the following information into clear categories.

Use these categories:

1. Main Topic
2. Benefits
3. Challenges
4. Important Concepts
5. Conclusion

Information:
{key_information}
"""

organized_information = ask_llm(prompt2)

print("\n===== STEP 2: ORGANIZED INFORMATION =====")
print(organized_information)


# ------------------------------------------------
# STEP 3: Generate summary
# ------------------------------------------------

prompt3 = f"""
Write a concise summary using the information below.

Requirements:
- 100 to 150 words
- Include the main topic
- Include important benefits
- Include important challenges
- Include the conclusion
- Do not add information that is not provided

Information:
{organized_information}
"""

summary = ask_llm(prompt3)

print("\n===== STEP 3: SUMMARY =====")
print(summary)


# ------------------------------------------------
# STEP 4: Improve summary
# ------------------------------------------------

prompt4 = f"""
Improve the following summary.

Requirements:
- Keep the original meaning
- Remove unnecessary repetition
- Make it clear and easy to understand
- Keep it between 100 and 150 words
- Do not introduce new facts

Summary:
{summary}
"""

final_summary = ask_llm(prompt4)

print("\n===== STEP 4: FINAL SUMMARY =====")
print(final_summary)