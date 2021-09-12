from peewee import *

from .base import BaseModel




class Currencyname(BaseModel):
    id = IntegerField(primary_key=True)
    sname = CharField()
    symbolcode = CharField()
    class Meta:
        db_table = 'currency'

class Currency(BaseModel):
    arcdate = CharField(primary_key=True)
    currency = ForeignKeyField(Currencyname, related_name='fk_id_curr', to_field='id')
    rate = FloatField()
    base = FloatField()
    class Meta:
        db_table = 'currencyrateall'

def get_currency(date_q: str):
    return Currency.filter(Currency.arcdate == date_q).first()


def list_currency(date_q: str):
    return list(Currency.select(Currency.arcdate,Currency.rate, Currency.base,
                                Currencyname.sname.alias('sname'),Currencyname.symbolcode.alias('symbolcode'))
                .join(Currencyname).where(Currency.arcdate == date_q))