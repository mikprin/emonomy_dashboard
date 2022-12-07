import pandas as pd
import numpy as np
import os, sys

import streamlit as st
import plotly.express as px

video_name = "Coppel Moda"

path_to_data = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "..", "example_data", "example_csv")

path_to_dynamics = os.path.join(path_to_data, "dynamics", f"{video_name}.csv")
raw_dynamics_dataframe = pd.read_csv(path_to_dynamics, index_col="Timestamp")
_ = raw_dynamics_dataframe.pop("Unnamed: 0")


st.set_page_config(page_title="Plotting template", page_icon="📈")


st.markdown(f"# Visualization for {video_name}")
st.sidebar.header(f"Visualization for {video_name}")
st.write(
    """18-25 GROUP: THE MAXIMUM NUMBER OF SMILES WAS 5%. HOWEVER , THE TREND
OF SMILES NUMBER WAS NEGATIVE FROM THE MIDDLE TO THE END OF THE VIDEO"""
)

st.bar_chart(raw_dynamics_dataframe)

