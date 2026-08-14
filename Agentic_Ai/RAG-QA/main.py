from retrieval import retrieve
from generate import generate_answer


question = input("Ask a question: ")

# Retrieve relevant documents
documents = retrieve(question)

# Combine retrieved documents
context = "\n\n".join(documents)

# Generate answer
answer = generate_answer(
    question,
    context
)

print("\nAnswer:")
print(answer)