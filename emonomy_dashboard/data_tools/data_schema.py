import pydantic
from typing import Optional


DATA_VERSION = '0.1.0'
class TableDefinition(pydantic.BaseModel):
    '''Definition for single table in schema'''
    table_name: str
    contents: str
    element_type: str

class StatementIrtResult(pydantic.BaseModel):
    '''pydantic model for statement IrtResult table'''
    video_id: str # Effectively a stimulus id
    message: str
    weight: float
    
class EmotionsMetricsRow(pydantic.BaseModel):
    '''One row of emotions metrics table'''
    video_id: str
    metrics: str
    value: float
class VideoDinamics(pydantic.BaseModel):
    '''Table for dynamics of one video'''
    Timestamp: list[int]
    ANGRY: list[float]
    CONFUSED: list[float]
    SAD: list[float]
    SURPRISED: list[float]
    DISGUSTED: list[float]
    FEAR: list[float]
    HAPPY: list[float]
    ENGAGEMENT: list[float]

class VideoDynamicDominanits(pydantic.BaseModel):
    """Table for dominant emotions of one video"""
    Timestamp: list[float]
    CALM: list[float]
    ANGRY: list[float]
    CONFUSED: list[float]
    SAD: list[float]
    SURPRISED: list[float]
    DISGUSTED: list[float]
    FEAR: list[float]
    HAPPY: list[float]

class Video(pydantic.BaseModel):
    '''Tables collection for one video'''
    video_id: str
    video_name: str
    video_file: str
    dynamics: VideoDinamics
    dynamicsDominants: VideoDynamicDominanits

class FastestExperimentData(pydantic.BaseModel):
    '''Root pydantic model for fastest experiment data'''
    version: str = DATA_VERSION
    client_id: str
    # schema: Optional[list[TableDefinition]] # Optional schema
    statement_irt_results: list[StatementIrtResult]
    emotions_data: list[EmotionsMetricsRow]
    videos: list[Video]