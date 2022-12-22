import pydantic


class TableDefinition(pydantic.BaseModel):
    table_name: str
    contents: str
    element_type: str

class StatementIrtResult(pydantic.BaseModel):
    stimulus: str
    message: str
    weight: float
    
class EmotionsData(pydantic.BaseModel):
    stimulus: str
    metrics: str
    value: float

class VideoDinamics(pydantic.BaseModel):
    time: float
    value: float

class Video(pydantic.BaseModel):
    video_name: str
    video_file: str
    dynamics: list

class FastestExperimentData(pydantic.BaseModel):
    version: str
    client_id: str
    schema: list[TableDefinition]
    statement_irt_results: StatementIrtResult
    emotions_data: EmotionsData
    videos: list[Video]