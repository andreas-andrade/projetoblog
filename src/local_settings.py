import os
PROJECT_ROOT_PATH = os.path.realpath(os.path.dirname(__file__))

LOCAL= False
DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASE_ENGINE = 'postgresql_psycopg2'
DATABASE_NAME = 'blog_db'
DATABASE_HOST = 'localhost'
DATABASE_USER = 'andreas'
DATABASE_PASSWORD = 'qwe'