from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from . import crud, database, schemas

app = FastAPI()


# ---------------- CREATE APPLICATION ----------------
@app.post(
    "/applications/",
    response_model=schemas.ApplicationResponse
)
def create_app(
    app_data: schemas.ApplicationCreate,
    db: Session = Depends(database.get_db)
):

    print("\n================ NEW REQUEST ================")
    print("📥 Incoming App:", app_data.app_name)

    result = crud.create_application(db, app_data)

    print("✅ Returning response to UI")
    print("===========================================\n")

    return result


# ---------------- GET APPLICATIONS ----------------
@app.get(
    "/applications/",
    response_model=list[schemas.ApplicationResponse]
)
def get_apps(db: Session = Depends(database.get_db)):

    print("📦 Fetching applications from DB")

    return crud.get_applications(db)


# ---------------- ROOT ----------------
@app.get("/")
def root():

    return {
        "message": "SecuRAG API Running",
        "status": "healthy"
    }