# Api for the emonomy dashboard control

import fastapi
import pandas as pd
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import os, sys

import dashboard_cluster_control
import dashboard_settings

try:
    settings = dashboard_settings.DashboardSettings()
except Exception as e:
    print("Error loading config file: {}".format(e))
    sys.exit(1)
    

app = fastapi.FastAPI(
    description="API for emonomy dashboard control",
    version="0.0.1",
)

@app.get("/list_dashboards")
def list_dashboards():
    dashboards = dashboard_cluster_control.list_dashboards()
    return {"dashboards": dashboards}

@app.post("/create_dashboard/{dashboard_name}")
    dashboards = dashboard_cluster_control.list_dashboards()
    if len(dashboards) < int(settings.config["General"]["max_workers"]):
        # Num of dashboards is less than max_workers creating a new one
        dashboard_cluster_control.create_dashboard()
        # return JSONResponse(status_code=200)
    else:
        pass