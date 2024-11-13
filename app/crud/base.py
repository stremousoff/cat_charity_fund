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
    async def push_to_db(project, session) -> None:
        await session.commit()
        await session.refresh(project)
        return project

    @staticmethod
    async def delete(db_object, session):
        await session.delete(db_object)
        await session.commit()
        return db_object

    @staticmethod
    async def patch(db_obj, obj_in, session):
        update_data = obj_in.dict(exclude_unset=True)
        for field in update_data:
            setattr(db_obj, field, update_data[field])
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj
