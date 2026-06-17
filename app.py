from flask import Flask, render_template, request, jsonify
from src.helper import download_embeddings
from src.prompt import prompt
from langchain_pinecone import PineconeVectorStore
from langchain_openai import ChatOpenAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

INDEX_NAME = "upchaar-medical-chatbot"

print("Loading embedding model...")
embeddings = download_embeddings()

print("Connecting to Pinecone index...")
docsearch = PineconeVectorStore.from_existing_index(
    index_name=INDEX_NAME,
    embedding=embeddings,
)

retriever = docsearch.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3},
)

llm = ChatOpenAI(model="gpt-4o", temperature=0.4)
question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)


@app.route("/")
def index():
    return render_template("chat.html")


@app.route("/get", methods=["POST"])
def chat():
    user_msg = request.form.get("msg", "").strip()
    if not user_msg:
        return jsonify({"answer": "Please enter a valid question."})

    response = rag_chain.invoke({"input": user_msg})
    return jsonify({"answer": response["answer"]})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=False)
