from typing import List, Dict

from fastapi import APIRouter, HTTPException, Query
import httpx

from fastapi.param_functions import Depends

from fastapi_movie_app.db.dao.dummy_dao import DummyDAO
from fastapi_movie_app.db.models.dummy_model import DummyModel
from fastapi_movie_app.web.api.dummy.schema import DummyModelDTO, DummyModelInputDTO

from ....settings import settings
import os



router = APIRouter()

@router.get("/movies/")
async def search_movies(
    title: str = Query(..., description="Guardians of the Galaxy Vol. 2"),
) -> List[Dict[str, str]]:

    OMDB_API_URL = "http://www.omdbapi.com/"

    params = {
        "apikey": settings.omdb_api_key,
        "s": title,
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(OMDB_API_URL, params=params)
        response.raise_for_status()
        data = response.json()

    if data["Response"] == "True":
        return data["Search"]
    else:
        raise HTTPException(status_code=404, detail="Movies not found on OMDB API")

