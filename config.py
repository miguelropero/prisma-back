from dotenv import load_dotenv
import os

load_dotenv()

user = os.environ["SQLALCHEMY_USER"]
password = os.environ["SQLALCHEMY_PASSWORD"]
host = os.environ["SQLALCHEMY_HOST"]
port = os.environ["SQLALCHEMY_PORT"]
database = os.environ["SQLALCHEMY_DATABASE"]

DATABASE_CONNECTION = f"postgresql://{user}:{password}@{host}:{port}/{database}"
