import os;
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    # SQL Database Configuration
    SQL_SERVER = os.environ.get('SQL_SERVER') or 'article-cms-server-[your-id].database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'article-cms-db'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'sqladmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or '[your-password]'
    
    SQLALCHEMY_DATABASE_URI = (
        'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + 
        '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + 
        '?driver=ODBC+Driver+17+for+SQL+Server'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Blob Storage Configuration
    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'articlecmsstorage[your-id]'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or '[your-connection-string]'
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'

    # Azure Active Directory Configuration
    CLIENT_ID = os.environ.get('CLIENT_ID') or '[your-client-id]'
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET') or '[your-client-secret]'
    AUTHORITY = os.environ.get('AUTHORITY') or 'https://login.microsoftonline.com/[your-tenant-id]'
    
    REDIRECT_PATH = '/getAToken'
    SCOPE = ['User.Read']
    SESSION_TYPE = 'filesystem'