import os
from pathlib import Path

from dotenv import load_dotenv

PATH_TO_ENV_FILE: str = '.env'
FULL_ENV_PATH = Path('/Users/flexerfadrigalan/Documents/Code/Python/FastAPI/Udemy Course - FastAPI - Flex - MyProject/flexboard/backend') / PATH_TO_ENV_FILE

# Loads the variables off the `.env` file
load_dotenv(dotenv_path=FULL_ENV_PATH)


class Config:
    # ------- Metadata ------- #
    PROJECT_TITLE: str = 'My FastAPI Project'
    PROJECT_VERSION: str = '0.0.1'
    AUTHOR: str = 'Flexer Fadrigalan'

    # ------- Database ------- #
    POSTGRES_USER: str = os.getenv('POSTGRES_USER')
    POSTGRES_PASSWORD: str = os.getenv('POSTGRES_PASSWORD')
    POSTGRES_SERVER: str = os.getenv('POSTGRES_SERVER')
    POSTGRES_PORT: str = os.getenv('POSTGRES_PORT')
    POSTGRES_DATABASE: str = os.getenv('POSTGRES_DATABASE')
    POSTGRES_DATABASE_URL: str = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DATABASE}"

    # ------------ JWT (JSON Web Token) Metadata ------------ #
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = os.getenv('JWT_ACCESS_TOKEN_EXPIRE_MINUTES')

    # The secret is generated by running: "openssl rand -hex 32"
    # You will get a string like: "609edbc55f9f9b066b4947416ffe0afc6809f6fba1decb5d5cc162a3f25d9093" - gibberish to us.
    JWT_SECRET_KEY: str = os.getenv('JWT_SECRET_KEY')

    # the value 'HS256' came from FastAPI docs, it is a hashing algorithm.
    JWT_ALGORITHM: str = os.getenv('JWT_ALGORITHM')


config_object: Config = Config()
