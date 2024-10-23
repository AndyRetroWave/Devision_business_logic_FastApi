import asyncio
import json

import aiofiles
import pytest
from sqlalchemy import insert

from app.bisnes_services.models.brands import Brands
from app.bisnes_services.models.categories import Categories
from app.bisnes_services.models.sneakers import Sneakers
from app.config import settings
from app.database import Base, async_session_maker, engine

LST_MODEL = [Brands, Categories, Sneakers]


@pytest.fixture(scope="session", autouse=True)
async def prepare_database():
    assert settings.MODE == "TEST"

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    async def open_mock_json(model: str):
        async with aiofiles.open(
            f"test/mock_data/mock_{model}.json", "r", encoding="utf-8"
        ) as f:
            return json.loads(await f.read())

    lst_json_model = ["brands", "categories", "sneakers"]
    task = []

    async def prepare_model_data(iter, json_model):
        async with async_session_maker() as session:
            smtp = insert(iter).values(await open_mock_json(json_model))
            await session.execute(smtp)
            await session.commit()

    for iter, json_model in zip(LST_MODEL, lst_json_model):
        task.append(asyncio.create_task(prepare_model_data(iter, json_model)))

    await asyncio.gather(*task)


@pytest.fixture(scope="session", autouse=True)
def event_loop(request):
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()
