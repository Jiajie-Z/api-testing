import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://reqres.in/api"
API_KEY = os.getenv("REQRES_API_KEY")