import pytest

from app.bisnes_services.repository.brands_services import BrandsService
from app.bisnes_services.shemas.brands_shemas import BrandsShemas

service = BrandsService()


@pytest.mark.asyncio
async def test_set_item():
    test_item = BrandsShemas(name="Nike2", country="USA")
    result = await service.set_item_brands(test_item)
    assert result is True


@pytest.mark.asyncio
async def test_get_brands_in_database():
    result = await service.get_all()
    assert isinstance(result, list)


@pytest.mark.asyncio
async def test_delete_brands():
    name_1 = "Nike2"
    name_2 = "Zoom"

    result_true = await service.delete(name_1)
    result_fake = await service.delete(name_2)

    assert result_true is True
    assert result_fake is False
