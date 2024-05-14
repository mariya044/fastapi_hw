from fastapi.templating import Jinja2Templates
from fastapi import APIRouter, Request, Form


router = APIRouter(
    prefix="/pages",
    tags=["Pages"]
)

templates = Jinja2Templates(directory='templates')


@router.get('/base')
def get_base_pages(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})


