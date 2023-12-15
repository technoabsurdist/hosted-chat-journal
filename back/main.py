from flask import Flask
from dotenv import load_dotenv
import os
import getpass
import chromadb

chroma_client = chromadb.Client()

os.environ['OPENAI_API_KEY'] = getpass.getpass('OpenAI API Key:')
app = Flask(__name__)

collection = chroma_client.create_collection(name="my_collection")

@app.route("/")
def home():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(debug=True)

@app.route('/submit')
def submit():
    # store your text, and handle tokenization, embedding, and indexing automatically
    collection.add(
        documents=["This is a document", "This is another document"],
        metadatas=[{"source": "my_source"}, {"source": "my_source"}],
        ids=["id1", "id2"]
    )

@app.route('/query')
def query():
    pass