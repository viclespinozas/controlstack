from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from uuid import UUID

from models.roles_model import Role
from schemas.roles_schema import RoleCreate, RoleUpdate


class RoleRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self) -> list[Role]:
        query = select(Role)

        result = await self.db.execute(query)
        return result.scalars().all()

    async def get_by_id(self, role_id: UUID) -> Role | None:
        query = (
            select(Role)
            .where(Role.id == role_id)
        )
        result = await self.db.execute(query)
        return result.scalar_one_or_none()

    async def create(self, payload: RoleCreate) -> Role:
        role = Role(
            **payload.model_dump()
        )
        self.db.add(role)
        await self.db.commit()
        await self.db.refresh(role)
        return role

    async def update(self, role: Role, payload: RoleUpdate) -> Role:
        update_data = payload.model_dump(exclude_none=True)

        for field, value in update_data.items():
            setattr(role, field, value)

        await self.db.commit()
        await self.db.refresh(role)
        return role