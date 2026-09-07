import ollama
import os

MODEL = "llama3.2-vision:latest"

# Ask for image filename
image_name = input("Enter image filename: ")

# Ask question
question = input("Ask a question about the image: ")

# Create image path
image_path = os.path.join("images", image_name)

# Check if image exists
if not os.path.exists(image_path):
    print("ERROR: Image not found.")

else:
    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": question,
                "images": [image_path]
            }
        ]
    )

    print("\nVISUAL QA ANSWER:")
    print(response["message"]["content"])