import os, sys
import pandas as pd
import streamlit as st
import plotly.express as px

from sqlalchemy import create_engine
from sqlalchemy.types import String, Integer, Float, Date, DateTime, Boolean

from dotenv import load_dotenv


path_to_data = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "..", "example_data", "example_csv")

# def create_db_connection(user, password, host, port, db_name):
#     os.environ["DB_HOST"] = "localhost"
#     database_string = f"postgresql://{user}:{password}@{host}:{port}/{db_name}"
#     engine = create_engine(database_string)
#     return engine

# # Get script path
script_path = os.path.realpath(__file__)
script_dir = os.path.dirname(script_path)
# env_folder = f"{script_dir}/../.env"
# load_dotenv(env_folder)  # take environment variables from .env.
# db_user = os.getenv('DB_USER')
# db_password = os.getenv('DB_PASSWORD')
# db_host = os.getenv('DB_HOST')
# db_port = os.getenv('DB_PORT')
# db_name = os.getenv('DB_NAME')

# engine = create_db_connection(db_user, db_password, db_host, db_port, db_name)

page_name = "Emonomy ashboard"

st.set_page_config(page_title=page_name, page_icon="📈", layout="wide")


# --- Sidebar ---
st.sidebar.title("Settings")


# st.dataframe(sample_df)


st.table()