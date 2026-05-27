from sqlalchemy import Column, Integer, String
from .database import Base


class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)

    app_name = Column(String)
    owner = Column(String)
    cloud_provider = Column(String)

    data_classification = Column(String)
    internet_exposed = Column(String)
    authentication_type = Column(String)
    encryption_enabled = Column(String)

    risk_score = Column(Integer)
    risk_level = Column(String)

    ai_summary = Column(String, default="⏳ AI processing...")

    ai_status = Column(String, default="processing")  # 🔥 NEW FIELD