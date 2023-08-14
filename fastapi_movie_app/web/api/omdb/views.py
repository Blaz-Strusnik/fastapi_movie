from typing import Dict, List

import httpx
from fastapi import APIRouter, Query

from fastapi_movie_app.settings import settings

router = APIRouter()


@router.get("/movies/")
async def search_movies(
    title: str = Query(..., description="Signs"),
) -> List[Dict[str, str]]:
    """
    Get's the movie data from OMDBApi.

    :param: title: title of movie

    :return: json data.
    """
    omdb_api_url = "http://www.omdbapi.com/"

    params = {
        "apikey": settings.omdb_api_key,
        "s": title,
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(omdb_api_url, params=params)
        response.raise_for_status()
        data = response.json()
        return data["Search"]
