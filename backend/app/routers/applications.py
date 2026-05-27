from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import get_db
from .. import schemas, crud


router = APIRouter(
    prefix="/applications",
    tags=["Applications"]
)


@router.post("/", response_model=schemas.ApplicationResponse)
def create_application(
    application: schemas.ApplicationCreate,
    db: Session = Depends(get_db)
):

    return crud.create_application(db, application)


@router.get("/", response_model=list[schemas.ApplicationResponse])
def get_applications(
    db: Session = Depends(get_db)
):

    return crud.get_applications(db)