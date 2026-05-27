from pydantic import BaseModel
from typing import Optional


class ApplicationCreate(BaseModel):
    app_name: str
    owner: str
    cloud_provider: Optional[str] = None
    data_classification: Optional[str] = None
    internet_exposed: Optional[str] = None
    authentication_type: Optional[str] = None
    encryption_enabled: Optional[str] = None


class ApplicationResponse(BaseModel):
    id: int
    app_name: str
    owner: str
    cloud_provider: Optional[str]
    data_classification: Optional[str]
    internet_exposed: Optional[str]
    authentication_type: Optional[str]
    encryption_enabled: Optional[str]
    risk_score: Optional[int]
    risk_level: Optional[str]
    ai_summary: Optional[str]

    class Config:
        from_attributes = True