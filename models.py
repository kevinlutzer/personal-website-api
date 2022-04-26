import datetime
import pytz
from sqlalchemy import VARCHAR, Column, Date, create_engine
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

from settings import DB_CA_CERT_PATH, DB_HOST, DB_MODE_DEV, DB_NAME, DB_PASSWORD, DB_USER

print(DB_CA_CERT_PATH)

DNS = "mysql+pymysql://%s:%s@%s:%d/%s?ssl_ca=%s" % (DB_USER, DB_PASSWORD, DB_HOST, 3306, DB_NAME, DB_CA_CERT_PATH)
if DB_MODE_DEV:
    DNS = "mysql+pymysql://%s:%s@%s:%d/%s" % (DB_USER, DB_PASSWORD, DB_HOST, 3306, DB_NAME)

engine = None
Session = sessionmaker(bind=engine)
Base = declarative_base()

engine = create_engine(
                        DNS,
                        echo='DEVEL' in os.environ,
                        pool_size=15)

Session = sessionmaker(bind=engine)

class Visitor(Base):

    __tablename__ = "visitor"

    ip = Column(VARCHAR(128), primary_key=True)
    type = Column(VARCHAR(128), nullable=False)
    created = Column(Date, nullable=False)

    @staticmethod
    def create(ip: str, type: str): 
        return Visitor(
            ip=ip,
            type=type,
            created=datetime.datetime.utcnow().replace(tzinfo=pytz.utc)
        )

Base.metadata.create_all(engine)
