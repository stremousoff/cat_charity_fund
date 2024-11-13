from typing import Optional

from fastapi import APIRouter
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import CharityProject

router = APIRouter()


class CRUDCharityProject(CRUDBase):
    @staticmethod
    async def get_project_id_by_name(
        project_name: str, session: AsyncSession
    ) -> Optional[int]:
        return (
            (
                await session.execute(
                    select(CharityProject.id).where(
                        CharityProject.name == project_name
                    )
                )
            )
            .scalars()
            .first()
        )


charity_crud = CRUDCharityProject(CharityProject)
