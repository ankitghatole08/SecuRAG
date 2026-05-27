from sqlalchemy.orm import Session
from . import models
from .ai_engine import generate_ai_risk_summary


def calculate_risk(app):

    score = 0

    if app.internet_exposed == "yes":
        score += 25
    if app.data_classification == "sensitive":
        score += 30
    if app.authentication_type == "password_only":
        score += 20
    if app.encryption_enabled == "no":
        score += 25

    if score >= 70:
        level = "Critical"
    elif score >= 50:
        level = "High"
    elif score >= 30:
        level = "Medium"
    else:
        level = "Low"

    return score, level


def create_application(db: Session, app_data):

    score, level = calculate_risk(app_data)

    # 🔥 SAVE FIRST (NO AI BLOCKING)
    db_app = models.Application(
        app_name=app_data.app_name,
        owner=app_data.owner,
        cloud_provider=app_data.cloud_provider,
        data_classification=app_data.data_classification,
        internet_exposed=app_data.internet_exposed,
        authentication_type=app_data.authentication_type,
        encryption_enabled=app_data.encryption_enabled,
        risk_score=score,
        risk_level=level,
        ai_summary="⏳ AI processing..."
    )

    db.add(db_app)
    db.commit()
    db.refresh(db_app)

    # 🔥 SAFE AI CALL (DO NOT BLOCK USER)
    try:
        ai_summary = generate_ai_risk_summary(app_data, level, score)

        db_app.ai_summary = ai_summary
        db.commit()

    except Exception as e:
        db_app.ai_summary = f"⚠ AI failed: {str(e)}"
        db.commit()

    return db_app


def get_applications(db: Session):
    return db.query(models.Application).all()