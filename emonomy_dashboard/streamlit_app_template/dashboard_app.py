import os
import sys
import pandas as pd
import streamlit as st
import plotly.express as px

from sqlalchemy import create_engine
from sqlalchemy.types import String, Integer, Float, Date, DateTime, Boolean

from dotenv import load_dotenv

# Pandas settings
pd.set_option("display.precision", 1)
pd.set_option('display.max_columns', None)

def import_settings():
    '''Create settings dictionary from source file'''
    settings_dict = {
        "dataframe_float_precision": 2, # Max float digits in dataframe
        "PATH_TO_DATA": "example_data/example_csv"
    }
    return settings_dict

def prepare_tabular_metrics_data(raw_emotions_dataframe):
    videos = raw_emotions_dataframe['stimulus'].unique()
    new_dataframe = pd.DataFrame(
        columns=raw_emotions_dataframe['metrics'].unique())
    for video in videos:
        mask = raw_emotions_dataframe["stimulus"] == video
        video_data = raw_emotions_dataframe[mask]
        for metric in video_data['metrics']:
            value = video_data[video_data["metrics"]
                               == metric]["value"].values[0]
            try:  # Try to convert to float
                value = str(
                    round(float(value), settings_dict["dataframe_float_precision"]))
            except:
                pass
            new_dataframe.loc[video, metric] = value
    return new_dataframe

def prepare_irt_metrics_data(raw_irt_dataframe):
    videos = raw_irt_dataframe['stimulus'].unique()
    new_dataframe = pd.DataFrame(
        columns=raw_irt_dataframe['message'].unique())
    for video in videos:
        mask = raw_irt_dataframe["stimulus"] == video
        video_data = raw_irt_dataframe[mask]
        for metric in video_data['message']:
            value = video_data[video_data["message"]
                               == metric]["weight"].values[0]
            try:  # Try to convert to float
                value = str(
                    round(float(value), settings_dict["dataframe_float_precision"]))
            except:
                pass
            new_dataframe.loc[video, metric] = value
    return new_dataframe




# # Get script path
script_path = os.path.realpath(__file__)
script_dir = os.path.dirname(script_path)

settings_dict = import_settings()


path_to_data = settings_dict["PATH_TO_DATA"]

# --- Load data ---

emotions_metrics = prepare_tabular_metrics_data(pd.read_csv(
    os.path.join(path_to_data, "emotions_metrics.csv"), index_col=0))

irt_metrics = prepare_irt_metrics_data(pd.read_csv(
    os.path.join(path_to_data, "statement_irt_result.csv"), index_col=0))

# --- Page view ---

page_name = "Emonomy dashboard"

st.set_page_config(page_title=page_name, page_icon="📈",
                   layout="wide",
                   )

# --- Sidebar ---
# st.sidebar.title("Settings")

st.markdown(f"# Emonomy report :bar_chart:")

# Draw tables

st.dataframe(emotions_metrics)

st.dataframe(irt_metrics)