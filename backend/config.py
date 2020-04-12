import os
from datetime import timedelta


class Config(object):
    #SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://sereb:selena253@localhost/MarkersetDB?driver=SQL+Server+Native+Client+11.0'
    SQLALCHEMY_DATABASE_URI = 'mssql+pymssql://u0979739_pythonbackend:E!10wv8r@31.31.196.234/u0979739_markersetdb'

    JWT_SECRET_KEY = "VerYsecreteKeY"
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=180)

    MAIL_SERVER = 'mail.hosting.reg.ru'
    MAIL_PORT = 587
    MAIL_USE_TLS = False
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'markerset@u0979739.plsk.regruhosting.ru'
    MAIL_DEFAULT_SENDER = 'markerset@u0979739.plsk.regruhosting.ru'
    MAIL_PASSWORD = 'nUE-G88-NiH-7AY'
