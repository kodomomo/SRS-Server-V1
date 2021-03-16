import os
from datetime import timedelta


class Config:
    SERVICE_NAME = 'SRS-V1'
    SECRET_KEY = os.getenv('SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=10)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(weeks=2)
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')


class DevelopmentConfig(Config):
    pass


class ProductionConfig(Config):
    pass


config = {
    'develop': DevelopmentConfig,
    'production': ProductionConfig
}