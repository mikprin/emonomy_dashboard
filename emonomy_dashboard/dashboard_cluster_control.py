
from pydantic import BaseModel
from datetime import datetime, timedelta


def list_dashboards():
    '''List all dashboards with format: \{ dashboard_port: client_id\ }'''
    dashboards = {}
    
    # Test example
    current_timestamp = datetime.now()
    d1 = Dashboard(dashboard_port=10001, client_id="1", last_update=current_timestamp).dict()
    dashboards = [d1,]
    return dashboards

def create_dashboard():
    '''Create a new dashboard'''
    pass

class Dashboard(BaseModel):
    dashboard_port: int
    client_id: str
    last_update: str