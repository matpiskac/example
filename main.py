"""Simple echo server"""

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory=".")


@app.get("/echo/{message}", response_class=HTMLResponse)
async def echo(request: Request, message: str):
    """Echo message through a template"""

    return templates.TemplateResponse(
        request=request, name="echo.html", context={"message": message}
    )
