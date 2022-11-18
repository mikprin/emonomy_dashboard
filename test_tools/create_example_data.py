# This scripts creates a small example dataset for the grafana
# and pushes it to postgresql

import os, sys
import pandas as pd
import sklearn.datasets
from sqlalchemy import create_engine
# 
from dotenv import load_dotenv

# Get script path
script_path = os.path.realpath(__file__)
script_dir = os.path.dirname(script_path)

# Get settings from .env
env_folder = f"{script_dir}/../.env"
load_dotenv(env_folder)  # take environment variables from .env.


# Pulling example data from the sklearn library
sklearn_data = sklearn.datasets.load_breast_cancer()
df = pd.DataFrame(sklearn_data.data, columns=sklearn_data.feature_names)


# Make database connection
os.environ["DB_HOST"] = "localhost"
database_string = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
engine = create_engine(database_string)

# Test tablename
table_name = "test_data"
    
df.to_sql(table_name, engine)