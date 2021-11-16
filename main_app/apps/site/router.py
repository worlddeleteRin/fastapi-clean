from fastapi import APIRouter

# from config import settings

# from database.main_db import db_provider

router = APIRouter(
    prefix = "/site",
    tags = ["site"],
)

@router.get("/test-endpoint")
def get_order_statusses(
):
    return {
        "success": True
    }

