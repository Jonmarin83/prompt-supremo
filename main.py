from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def form_get(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/", response_class=HTMLResponse)
async def form_post(request: Request, user_input: str = Form(...)):
    prompt = f"PROMPT SUPREMO V2.1\n\n{user_input}\n\n[Inspección visual y control de calidad activado]"
    return templates.TemplateResponse("index.html", {"request": request, "result": prompt})

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
