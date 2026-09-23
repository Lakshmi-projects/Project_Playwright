import os
from dotenv import load_dotenv
#env
env = os.getenv("demo_webshop", "qa")
load_dotenv(f".env.{env}")
BASE_URL = os.getenv("BASE_URL")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

