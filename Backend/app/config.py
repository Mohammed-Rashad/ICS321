import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', '3d7c7f55cc6748a793d1c86a73bb29dd')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', '3d7c7f55cc6748a793d1c86a73bb29dd')
    JWT_ACCESS_TOKEN_EXPIRES = 3600  # Tokens expire in 1 hour
    DATABASE_URI = os.getenv('DATABASE_URI', 'mysql+pymysql://root:FreeSyria:)@localhost/TRAIN_MANAGEMENT_SYSTEM')
