import ollama

# Get research topic from user
topic = input("Enter research topic: ")

# STEP 1: Create research plan
plan = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": f"Create a 3-step research plan for {topic}."
        }
    ]
)["message"]["content"]


# STEP 2: Create draft report
draft = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": f"Write a short report using this plan:\n{plan}"
        }
    ]
)["message"]["content"]


# STEP 3: Review and improve
reflection = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": f"Review and suggest improvements:\n{draft}"
        }
    ]
)["message"]["content"]


# Display results
print("\nPLAN:\n", plan)
print("\nDRAFT:\n", draft)
print("\nREFLECTION:\n", reflection)