# from fastapi import FastAPI from functools import lru_cache
from functools import lru_cache

from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database

from config import settings

from pydantic import BaseModel


class DbProvider(BaseModel):
    db_client: MongoClient
    db_main: Database 

    some_db: Collection

    class Config:
        arbitrary_types_allowed = True


@lru_cache
def setup_db_main() -> DbProvider:
    print('call setup db_main function')
    db_client  = MongoClient(settings.DB_URL)
    db_main = db_client[settings.DB_NAME]
    db_provider = DbProvider(
                db_client = db_client,
                db_main = db_main,
                some_db = db_main["db_name"], 
            )
    return db_provider

db_provider = setup_db_main()

