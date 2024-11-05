import streamlit as st
import base64
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
print("Loaded OpenAI API Key:", os.getenv('OPENAI_API_KEY'))
