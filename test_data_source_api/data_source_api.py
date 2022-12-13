# Simplt fastAPI data source

# Path: data_source_api.py
import fastapi
import pandas as pd
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import os, sys

json_compatible_item_data = {"name": "Foo", "price": 50.2, "is_offer": None}

users = [1,2,3,4,5,6,7,8,9,10]

path_to_script = os.path.realpath(os.path.realpath(__file__))
# Settings
path_to_data = os.path.join( path_to_script , "../example_data/example_csv" )

# Create result dict
pandases = {}
# Don't forget to add check for the shema name occupied
pandases["database_schema"] = pd.DataFrame()

database_schema_dict = {}

def get_dataframes_from_csv_folder(pandases_dict , path_to_data , parent_folder = None):
    '''Recurcively read all dataframes to one dict'''
    for file in os.listdir(path_to_data):
        full_path = os.path.join( path_to_data, file)
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

pandases = get_dataframes_from_csv_folder(pandases.copy() , path_to_data)

api_app = fastapi.FastAPI(
    description="Test data source API for emonomy",
    version="0.0.1",
)

@api_app.get("/get_user_metrics/{user_id}")
async def get_user_metrics(user_id: int):
    if user_id not in users:
        raise fastapi.HTTPException(status_code=404, detail="User not found")
    return JSONResponse(content=json_compatible_item_data)
        