import os
from dotenv import load_dotenv

load_dotenv()

class Settings():
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    MODEL_NAME = "llama-3.1-8b-instant"
    TEMPERATURE = 0.9 #as we are making questions so we want our model to be more creative
    MAX_RETRIES = 3 #if api calls,the number of times to try

settings = Settings()

