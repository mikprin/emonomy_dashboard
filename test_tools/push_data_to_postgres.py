# This script can push data to postgres database
import os, sys
import argparse
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.types import String, Integer, Float, Date, DateTime, Boolean
from dotenv import load_dotenv

def create_connection(user, password, host, port, db_name):
    os.environ["DB_HOST"] = "localhost"
    database_string = f"postgresql://{user}:{password}@{host}:{port}/{db_name}"
    engine = create_engine(database_string)
    return engine

def get_dataframes_from_csv_folder(pandases_dict , path_to_data , parent_folder = None):
    '''Recurcively read all dataframes to one dict'''
    
    # Create result dict
    pandases = {}
    
    # Don't forget to add check for the shema name occupied
    pandases["database_schema"] = pd.DataFrame()
    
    for file in os.listdir(path_to_data):
        full_path = os.path.join( path_to_data, file)
        database_schema_dict = {}
        
        if os.path.isfile(full_path):
            # Do stuff with files
            filename_no_extention = file.split('.')[0]
            
            if parent_folder:
                database_schema_dict["parent_folder"] = parent_folder
                database_schema_dict["table_name"] = f"{parent_folder}_{filename_no_extention}"
                dataframe_key = f"{parent_folder}_{filename_no_extention}"
            else:
                database_schema_dict["parent_folder"] = ""
                database_schema_dict["table_name"] = filename_no_extention
                dataframe_key = filename_no_extention
            print(f"Adding: {file} to {filename_no_extention}")
            dataframe = pd.read_csv( full_path , index_col=0 )
            pandases_dict[dataframe_key] = dataframe
            database_schema_dict["colomns"] = list(dataframe.columns)
            # Create schema colomn and push data about this table there.
            series = pd.Series(database_schema_dict)
            pandases["database_schema"][database_schema_dict["table_name"]] = series
            
        elif ( os.path.isdir ( full_path ) ):
            # Do stuff with dirs
            print(f"Dir {file}")
            get_dataframes_from_csv_folder(pandases_dict , full_path , parent_folder = file )
    return pandases_dict

def push_data_to_postgres(data_path, engine):
    pass

if __name__ == "__main__":
    
    # Get script path
    script_path = os.path.realpath(__file__)
    script_dir = os.path.dirname(script_path)
    
    # Default data path
    data_path = f"{script_dir}/../data"
    
    # Parse CMD arguments
    parser = argparse.ArgumentParser()
    
    parser.add_argument("--data" , "-d", help="set path to data file", default=f"{script_dir}/../data")
    
    args = parser.parse_args()
    
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