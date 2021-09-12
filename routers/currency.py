from typing import Any, List

import peewee
from fastapi import APIRouter, HTTPException, Response, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from models.currency import get_currency, list_currency
from pydantic import BaseModel
from pydantic.utils import GetterDict

router_currency = APIRouter(
    prefix="/currency",
    tags=["currency"]
)


class PeeweeGetterDict(GetterDict):
    def get(self, key: Any, default: Any = None):
        res = getattr(self._obj, key, default)
        if isinstance(res, peewee.ModelSelect):
            return list(res)
        return res


class CurrencyModel(BaseModel):
    arcdate: str
    # currency_id: str
    # sname: str
    # symbolcode: str
    rate: float
    base: float

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict

class CurrencyNameModel(BaseModel):
    id: int
    sname:str
    symbolcode:str
    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict

@router_currency.get("/exchange/{date_q}", response_model=List[CurrencyModel], summary="Returns a single currency")
async def get_exchange(date_q: str):
    """
    Перегляд валют:
    :param date_q: "DD.MM.YYYY"
    :return:
    """
    return list_currency(date_q)

@router_currency.get("/exchange/")
async def get_exchange():
    """
    Перегляд валют:
    """
    return Response(status_code=200)
