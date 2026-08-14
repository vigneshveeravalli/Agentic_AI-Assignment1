import requests


def generate_answer(question, context):

    prompt = f"""
You are a helpful question-answering assistant.

Answer the question using ONLY the provided context.

If the answer is not present in the context, say:
"I don't know based on the provided information."

Context:
{context}

Question:
{question}

Answer:
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2",
            "prompt": prompt,
            "stream": False
        }
    )

    result = response.json()

    return result["response"]