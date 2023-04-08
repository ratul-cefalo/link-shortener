from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional
from sqlalchemy.orm import Session
from .db import Link
from .utils import generate_short_code

# Create the FastAPI app
app = FastAPI()

# Define the input model
class LinkRequest(BaseModel):
    long_url: str

# Define the output model
class LinkResponse(BaseModel):
    short_url: str

def get_db():
    db = Session(...)
    try:
        yield db
    finally:
        db.close()


# Define the API endpoint to create a shortened URL
@app.post("/api/v1/shorten", response_model=LinkResponse)
async def shorten_link(link: LinkRequest, db: Session = Depends(get_db)):
    short_code = generate_short_code()

    # Store the long URL and short code in the database
    db_link = Link(long_url=link.long_url, short_code=short_code)
    db.add(db_link)
    db.commit()
    db.refresh(db_link)

    # Return the shortened URL
    short_url = request.url_for("redirect_to_long_url", short_code=short_code)
    return {"short_url": short_url}

# Define the API endpoint to redirect to the long URL
@app.get("/{short_code}")
async def redirect_to_long_url(short_code: str, db: Session = Depends(get_db)):
    db_link = db.query(Link).filter(Link.short_code == short_code).first()
    if db_link:
        return RedirectResponse(db_link.long_url)
    else:
        raise HTTPException(status_code=404, detail="Link not found")
