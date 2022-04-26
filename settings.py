import os
from typing import Tuple

API_MODE_DEV = os.environ.get("API_MODE") == 'dev'
DB_MODE_DEV = os.environ.get("DB_MODE") == 'dev'

def get_ca_cert_path() -> str: 
    """get_ca_cert_path gets the cert path based on if we are in a development"""
    path = 'ca_cert/core-ca-certificate.crt'
    if API_MODE_DEV:
        return path

    # defimed with a secret in k8s/deployment
    return '/etc/db-ca-cert/core-ca-certificate.crt'


def get_db_creds() -> Tuple[str, str, str, str]: 
    """get_db_creds returns a tuple representing access information for the db"""

    db_host: str
    db_user: str
    db_password: str

    if DB_MODE_DEV:
        db_host = 'localhost'
        db_user = 'personal-website-api'
        db_password = '6SxFen6wvZTzv7Knh5vv9QCgVo0='

        return (db_host, db_user, db_password)

    db_host = os.environ.get("DB_HOST")
    db_user = os.environ.get("DB_USER")
    db_password = os.environ.get("DB_PASSWORD")

    
    if not db_host:
        raise ValueError("DB_HOST must be specified in the environment")

    if not db_user:
        raise ValueError("DB_USER must be specified in the environment")

    if not db_password:
        raise ValueError("DB_PASSWORD must be specified in the environment")


    return (db_host, db_user, db_password)

DB_NAME = "personalwebsite"
DB_CA_CERT_PATH = get_ca_cert_path()

# Get db creds from env
(DB_HOST, DB_USER, DB_PASSWORD) = get_db_creds()