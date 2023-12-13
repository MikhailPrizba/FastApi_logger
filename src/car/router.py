from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from base import get_async_session
from .models import Car
from .schema import CarCreate

router = APIRouter(prefix="/cars", tags=["Cars"])


@router.get("")
async def get_specific_operations(
    session: AsyncSession = Depends(get_async_session),
):
    try:
        query = select(Car)
        result = await session.execute(query)
        return {"status": "success", "data": result.scalars().all(), "details": None}
    except Exception:
        # Передать ошибку разработчикам
        raise HTTPException(
            status_code=500, detail={"status": "error", "data": None, "details": None}
        )


@router.post("")
async def add_specific_operations(
    new_operation: CarCreate, session: AsyncSession = Depends(get_async_session)
):
    stmt = insert(Car).values(**new_operation.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}
