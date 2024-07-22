from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
from typing import Optional
from app.models import mongodb
from app.models.book import BookModel

import os 

# 현재파일의 경로 그리고 이 파일의 부모를 의미 
# BASE_DIR = Path(__file__).reslove().parent.parnet 부모의 부모 
BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()
templates = Jinja2Templates(directory=BASE_DIR /"templates")

@app.on_event("startup")
async def on_app_start():
	print("========서버시작========")
	mongodb.connect()

@app.on_event("shutdown")
async def on_app_shutdown():
	print("========서버종========")
	mongodb.close()

@app.get("/")
async def read_item(request: Request):
	book = BookModel(keyword="파이썬", publisher="출판사", price="1999", img="ddddd.com")
	print(await mongodb.engine.save(book))
	return templates.TemplateResponse(
		"./index.html", {"request":request, "title":" 콜렉터 북북"})
	

@app.get("/search", response_class=HTMLResponse)
def search(request:Request, q:Optional[str]=None):
	print(q,'<<<<<<')
	return templates.TemplateResponse(
		"./index.html", {"request":request, "title":" 콜렉터 북북"})


@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
	print(request.headers,'<')
	return templates.TemplateResponse(
	request=request, name="item.html", context={"id": id, "data":"hi"}
	)