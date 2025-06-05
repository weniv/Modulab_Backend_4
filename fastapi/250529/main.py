from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

notices = ["공지사항1", "공지사항2", "공지사항3"]

templates = Jinja2Templates(directory="templates")  # templates 폴더를 지정합니다.


@app.get("/")  # -> 127.0.0.1:8000 get method
def read_root():
    return {"Hello": "World!"}


@app.get("/about")  # -> 127.0.0.1:8000/about get method
def about():
    return {"message": "about page"}


@app.get("/contact")  # -> 127.0.0.1:8000/contact get method
def contact():
    return {"message": "contact page"}


@app.get("/notice")  # -> 127.0.0.1:8000/notice get method
def notice():
    return {"notice": notices}


@app.get("/index", response_class=HTMLResponse)
def index():
    return "<h1> 너무 더웡어어어엉어어어어 하겐다즈 줘어엉 </h1>"


@app.get("/index2")  # -> 127.0.0.1:8000/index2 get method
def index2(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
