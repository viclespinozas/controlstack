from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID

from core.config import get_db
from schemas.roles_schema import RoleCreate, RoleUpdate, RoleResponse
from repositories.roles_repository import RoleRepository

router = APIRouter(prefix="/api/roles", tags=["Roles"])

# Temporary stand-in for the authenticated user_id.
# Replace this with your actual JWT dependency once auth is implemented.
TEMP_USER_ID = UUID("9d025864-1992-4db2-9d6a-38a52ddbe6af")


def get_repo(db: AsyncSession = Depends(get_db)) -> RoleRepository:
    return RoleRepository(db)


@router.get("/", response_model=list[RoleResponse])
async def get_expenses(
    repo: RoleRepository = Depends(get_repo)
):
    return await repo.get_all()


@router.get("/{role_id}", response_model=RoleResponse)
async def get_expense(
    role_id: UUID,
    repo: RoleRepository = Depends(get_repo)
):
    role = await repo.get_by_id(role_id)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    return role


@router.post("/", response_model=RoleResponse, status_code=201)
async def create_role(
    payload: RoleCreate,
    repo: RoleRepository = Depends(get_repo)
):
    return await repo.create(payload=payload)


@router.put("/{role_id}", response_model=RoleResponse)
async def update_expense(
    role_id: UUID,
    payload: RoleUpdate,
    repo: RoleRepository = Depends(get_repo)
):
    role = await repo.get_by_id(role_id)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")

    if not payload.model_dump(exclude_none=True):
        raise HTTPException(status_code=400, detail="No update fields provided")

    return await repo.update(role, payload)


@router.delete("/{role_id}", status_code=204)
async def delete_role(
    role_id: UUID,
    repo: RoleRepository = Depends(get_repo)
):
    role = await repo.get_by_id(role_id)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")

    await repo.delete(role)