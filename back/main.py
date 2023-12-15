from dotenv import load_dotenv
import os
from langchain.embeddings import OpenAIEmbeddings

load_dotenv()

embeddings_model = OpenAIEmbeddings()
