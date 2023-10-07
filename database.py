from sqlalchemy import create_engine
from dotenv import load_dotenv
load_dotenv()
import os

db_connection_string = "mysql+pymysql://%s:%s@%s/%s?charset=utf8mb4" % (os.getenv("DB_USERNAME"), os.getenv("DB_PASSWORD"), os.getenv("DB_HOST"), os.getenv("DB_NAME"))
engine = create_engine(
    db_connection_string,
    connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    }
)

