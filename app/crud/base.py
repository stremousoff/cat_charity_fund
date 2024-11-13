from datetime import datetime

from sqlalchemy import select, asc


class CRUDBase:
    def __init__(self, model):
        self.model = model

    async def get_object(self, object_id, session):
        return (
            (
                await session.execute(
                    select(self.model).where(self.model.id == object_id)
                )
            )
            .scalars()
            .first()
        )

    async def get_all_objects(self, session):
        return (await session.execute(select(self.model))).scalars().all()

    async def get_all_objects_is_unclosed(self, session):
        return (
            (
                await session.execute(
                    select(self.model)
                    .where(self.model.fully_invested == 0)
                    .order_by(asc("create_date"))
                )
            )
            .scalars()
            .all()
        )

    async def create(self, obj_in, session, user=None, skip_commit=False):
        obj_in_data = obj_in.dict()
        if user is not None:
            obj_in_data["user_id"] = user.id
        creat_obj_for_db = self.model(**obj_in_data)
        session.add(creat_obj_for_db)
        if not skip_commit:
            await session.commit()
            await session.refresh(creat_obj_for_db)
        return creat_obj_for_db

    @staticmethod
    async def push_to_db(project, session):
        await session.commit()
        await session.refresh(project)
        return project

    @staticmethod
    async def delete(db_object, session):
        await session.delete(db_object)
        await session.commit()
        return db_object

    @classmethod
    async def patch(cls, db_obj, obj_in, session):
        update_data = obj_in.dict(exclude_unset=True)
        for field in update_data:
            setattr(db_obj, field, update_data[field])
        if db_obj.full_amount == db_obj.invested_amount:
            db_obj.fully_invested = True
            db_obj.close_date = datetime.now()
        return await cls.push_to_db(db_obj, session)
