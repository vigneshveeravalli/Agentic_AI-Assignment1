import chromadb
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to database
client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_collection(
    name="company_documents"
)


def retrieve(question, number_of_results=3):

    # Convert question into embedding
    question_embedding = model.encode(
        question
    ).tolist()

    # Search vector database
    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=number_of_results
    )

    return results["documents"][0]


if __name__ == "__main__":

    question = input("Ask a question: ")

    documents = retrieve(question)

    print("\nRetrieved information:\n")

    for document in documents:
        print("-", document)