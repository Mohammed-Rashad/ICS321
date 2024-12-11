import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key_here')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'your_jwt_secret_key')
    DATABASE_URI = os.getenv('DATABASE_URI', 'mysql://user:password@localhost/dbname')
