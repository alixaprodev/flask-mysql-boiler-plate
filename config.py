# config.py
import os
import pyodbc
class Config:
    SECRET_KEY = 'your_secret_key'
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///site.sqlite'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://root:root@ALI/hireasy?driver=ODBC+Driver+18+for+SQL+Server&ssl=true&TrustServerCertificate=yes'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
