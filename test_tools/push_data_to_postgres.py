# This script can push data to postgres database
import os, sys

import argparse

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.types import String, Integer, Float, Date, DateTime, Boolean


def create_connection(user, password, host, port, db_name):
    os.environ["DB_HOST"] = "localhost"
    database_string = f"postgresql://{user}:{password}@{host}:{port}/{db_name}"
    engine = create_engine(database_string)
    return engine




def push_data_to_postgres(data_path, engine):
    pass


if name == "__main__":
    
    # Get script path
    script_path = os.path.realpath(__file__)
    script_dir = os.path.dirname(script_path)
    
    # Default data path
    data_path = f"{script_dir}/../data"
    
    # Parse CMD arguments
    parser = argparse.ArgumentParser()
    
    parser.add_argument("--data" , "-d", help="set path to data file", default=f"{script_dir}/../data")
    
    
    parser.parse_args()
    
    if args.data:
        data_path = args.data
    
    # Get settings from .env
    env_folder = f"{script_dir}/../.env"
    load_dotenv(env_folder)  # take environment variables from .env.
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_host = os.getenv('DB_HOST')
    db_port = os.getenv('DB_PORT')
    db_name = os.getenv('DB_NAME')
    
    engine = create_connection(db_user, db_password, db_host, db_port, db_name)
    
    push_data_to_postgres(data_path, engine)