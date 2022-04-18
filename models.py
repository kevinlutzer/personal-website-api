import datetime
import pytz
from sqlalchemy import VARCHAR, Column, Date, create_engine
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# from sqlalchemy.`` import fun
import os

engine = None
Session = sessionmaker(bind=engine)
Base = declarative_base()

engine = create_engine(
                        "mysql+pymysql://%s:%s@%s:%d/%s?ssl_ca=ca_cert/core-ca-certificate.crt" % ("linroot", "b7YVdx1jFLPM&nfR", "lin-1617-1707-mysql-primary.servers.linodedb.net", 3306, "personalwebsite"),
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

    # @classmethod
    # def get_type_quantities(cls, session: Session): 
    #     return session.query(cls.).

Base.metadata.create_all(engine)
