from pydantic import BaseModel, Field
from typing import Optional, List

class Movie(BaseModel):
    id: int = Field(..., title="ID of the movie", description="Unique identifier for the movie")
    title: str = Field(..., title="Title of the movie", description="Title of the movie")
    description: str = Field(..., title="Description of the movie", description="Description of the movie")
    year: int = Field(..., title="Year of the movie", description="Year of release")
    rating: float = Field(..., title="Rating of the movie", description="Rating of the movie")
    genres: List[str] = Field(..., title="Genres of the movie", description="List of genres associated with the movie")
    