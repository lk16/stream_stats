#!/usr/bin/env python

from starlette.applications import Starlette
from starlette.responses import JSONResponse, HTMLResponse, Response
from starlette.requests import Request
from starlette.routing import Route, Mount
from starlette.staticfiles import StaticFiles
import uvicorn
from pathlib import Path

FORM_HTML = Path('static/form.html').read_text()
STATS_FILE = Path("stats.txt")


async def show_form(request: Request) -> HTMLResponse:
    return HTMLResponse(FORM_HTML)


async def get_stats(request: Request) -> JSONResponse:
    try:
        stats = STATS_FILE.read_text()
    except FileNotFoundError:
        stats = ""

    return JSONResponse({"stats": stats})


async def update_stats(request: Request) -> Response:
    body = await request.json()
    stats = body["stats"]
    STATS_FILE.write_text(stats)
    return Response()


app = Starlette(debug=True, routes=[
    Route('/', show_form),
    Route('/stats', get_stats, methods=["GET"]),
    Route('/stats', update_stats, methods=["PATCH"]),
    Mount('/static', app=StaticFiles(directory='static'), name="static")

])


if __name__ == "__main__":
    uvicorn.run(app)
