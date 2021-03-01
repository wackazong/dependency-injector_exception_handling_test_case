from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide

from api.services.listener_count import Add
from api.containers import Application

router = APIRouter(
    responses={404: {"description": "Not found"}},
)


@router.get("/")
@inject
async def listener_post(
    add: Add = Depends(Provide[Application.usecases.listener_count.add]),
) -> None:

    add.execute()
