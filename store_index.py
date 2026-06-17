from src.helper import load_pdf_files, text_split, download_embeddings
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
INDEX_NAME = "upchaar-medical-chatbot"
BATCH_SIZE = 64  # chunks per Pinecone upsert — keeps each request well under 4 MB

print("Loading PDF files...")
extracted_data = load_pdf_files("data/")
print(f"Loaded {len(extracted_data)} pages.")

print("Splitting into chunks...")
text_chunks = text_split(extracted_data)
print(f"Created {len(text_chunks)} chunks.")

print("Loading embedding model...")
embeddings = download_embeddings()

print("Connecting to Pinecone...")
pc = Pinecone(api_key=PINECONE_API_KEY)

if not pc.has_index(INDEX_NAME):
    print(f"Creating index '{INDEX_NAME}'...")
    pc.create_index(
        name=INDEX_NAME,
        dimension=1024,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1"),
    )
else:
    print(f"Index '{INDEX_NAME}' already exists.")

print(f"Uploading {len(text_chunks)} chunks in batches of {BATCH_SIZE}...")
total_batches = (len(text_chunks) + BATCH_SIZE - 1) // BATCH_SIZE

for i in range(0, len(text_chunks), BATCH_SIZE):
    batch = text_chunks[i : i + BATCH_SIZE]
    batch_num = (i // BATCH_SIZE) + 1
    print(f"  Batch {batch_num}/{total_batches} ({len(batch)} chunks)...")

    if i == 0:
        docsearch = PineconeVectorStore.from_documents(
            documents=batch,
            embedding=embeddings,
            index_name=INDEX_NAME,
        )
    else:
        docsearch.add_documents(batch)

print("Done! Index stored successfully.")
