import chromadb
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Create ChromaDB client
client = chromadb.PersistentClient(path="./chroma_db")

# Create collection
collection = client.get_or_create_collection(
    name="company_documents"
)

# Read document
with open("documents/company.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Split document into chunks
chunks = [
    chunk.strip()
    for chunk in text.split("\n\n")
    if chunk.strip()
]

# Create embeddings
embeddings = model.encode(chunks).tolist()

# Add documents to vector database
for i, chunk in enumerate(chunks):

    collection.upsert(
        ids=[f"doc_{i}"],
        documents=[chunk],
        embeddings=[embeddings[i]]
    )

print("Indexing completed!")
print("Number of chunks:", len(chunks))