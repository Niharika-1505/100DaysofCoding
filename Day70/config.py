import os
import re

from dotenv import load_dotenv

# read key-value pairs from the .env file and store them as environment variables
load_dotenv()

# Gmail credentials
SMTP_LOGIN = os.environ["My_EMAIL"]
SMTP_PASS = os.environ["My_SecretKey"]
# SMTP_LOGIN = os.environ.get("My_EMAIL")
# SMTP_PASS = os.environ.get("My_SecretKey")

# secret key
# SECRET_KEY = os.environ.get("SECRET_KEY")
SECRET_KEY = os.environ["SECRET_KEY"]

# Heroku PostgreSQL URL
# if DATABASE_URL variable is not set, it will use the DB file instead
DATABASE_URL = "sqlite:///blog.db"
# DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///blog.db")  # or other relevant config var
# print(DATABASE_URL)
# if DATABASE_URL.startswith("postgres://"):
#     DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

