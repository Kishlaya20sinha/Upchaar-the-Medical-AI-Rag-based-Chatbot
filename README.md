# 🏥 Upchaar – Medical AI RAG Chatbot

Upchaar is an **AI-powered Medical Chatbot** built using **LLMs, LangChain, Pinecone, and Flask**.
It uses **Retrieval-Augmented Generation (RAG)** to answer medical queries by retrieving relevant medical information and generating intelligent responses using a Large Language Model.

This project demonstrates how to build a **production-ready AI chatbot** with vector databases, embeddings, and cloud deployment using AWS.

---

# 🚀 Features

* 🤖 AI-powered medical chatbot
* 🔎 Retrieval-Augmented Generation (RAG)
* 🧠 Embedding-based document search
* 📚 Vector database storage using Pinecone
* 🌐 Web interface using Flask
* ☁️ Deployment-ready architecture using AWS & Docker
* 🔁 CI/CD using GitHub Actions

---

# 🧰 Tech Stack

* **Python**
* **LangChain**
* **OpenAI GPT**
* **Pinecone Vector Database**
* **Flask**
* **Docker**
* **AWS (EC2 + ECR)**
* **GitHub Actions (CI/CD)**

---

# ⚙️ Project Setup

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/Kishlaya20sinha/Upchaar-the-Medical-AI-Rag-based-Chatbot.git
cd Upchaar-the-Medical-AI-Rag-based-Chatbot
```

---

# 🐍 Step 1 – Create Conda Environment

```bash
conda create -n medibot python=3.10 -y
```

Activate the environment:

```bash
conda activate medibot
```

---

# 📦 Step 2 – Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Step 3 – Add Environment Variables

Create a `.env` file in the **root directory** and add the following credentials:

```ini
PINECONE_API_KEY="xxxxxxxxxxxxxxxxxxxxxxxx"
OPENAI_API_KEY="xxxxxxxxxxxxxxxxxxxxxxxx"
```

---

# 🧠 Step 4 – Store Embeddings in Pinecone

Run the following command to create embeddings and store them in Pinecone:

```bash
python store_index.py
```

---

# ▶️ Step 5 – Run the Application

```bash
python app.py
```

Now open your browser and go to:

```bash
http://localhost:5000
```

---

# ☁️ AWS CI/CD Deployment with GitHub Actions

## 1️⃣ Login to AWS Console

Go to the AWS Management Console.

---

## 2️⃣ Create an IAM User for Deployment

Give the IAM user the following access:

### Required Services

* **EC2** – Virtual machine to host the application
* **ECR** – Store Docker images

### Required Policies

* `AmazonEC2ContainerRegistryFullAccess`
* `AmazonEC2FullAccess`

---

## 3️⃣ Create an ECR Repository

Create a repository to store the Docker image.

Example repository URI:

```
315865595366.dkr.ecr.us-east-1.amazonaws.com/medicalbot
```

Save this URI for later use.

---

## 4️⃣ Launch an EC2 Instance

Create an **Ubuntu EC2 instance**.

---

## 5️⃣ Install Docker on EC2

Run the following commands inside the EC2 instance:

```bash
sudo apt-get update -y
sudo apt-get upgrade
```

Install Docker:

```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```

Allow Docker usage without sudo:

```bash
sudo usermod -aG docker ubuntu
newgrp docker
```

---

## 6️⃣ Configure EC2 as a Self-Hosted Runner

Go to your GitHub repository:

```
Settings → Actions → Runners → New Self Hosted Runner
```

Select **Linux** and run the commands provided by GitHub on your EC2 machine.

---

## 7️⃣ Configure GitHub Secrets

Add the following secrets in your GitHub repository:

```
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_DEFAULT_REGION
ECR_REPO
PINECONE_API_KEY
OPENAI_API_KEY
```

These secrets allow GitHub Actions to automatically deploy the project.

---

# 📂 Project Structure

```
Upchaar-the-Medical-AI-Rag-based-Chatbot
│
├── src/                # Source code
├── research/           # Experiments and notebooks
├── app.py              # Flask application
├── store_index.py      # Embedding generation and storage
├── requirements.txt    # Project dependencies
├── setup.py            # Package configuration
├── template.sh         # Project folder structure script
└── README.md
```

---

# 🎯 Future Improvements

* Medical knowledge base expansion
* Better prompt engineering
* UI improvements
* Chat history support
* Multi-language support

---

# 👨‍💻 Author

**Kishlaya Sinha**

B.Tech CSE | Birla Institute of Technology, Mesra (Patna Campus)

* GitHub: https://github.com/Kishlaya20sinha
* LinkedIn: https://www.linkedin.com/in/kishlaya-sinha-9134a0211/

---

⭐ If you like this project, consider giving it a **star on GitHub!**
