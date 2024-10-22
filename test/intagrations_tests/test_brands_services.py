import pytest

from app.bisnes_services.repository.brands_services import BrandsService
from app.bisnes_services.shemas.brands_shemas import BrandsShemas

service = BrandsService()


@pytest.mark.asyncio
async def test_set_brands_in_database():
    test_item = BrandsShemas(name="Nike2", country="USA")
    result = await service.set_brands_in_database(test_item)
    assert result is True


@pytest.mark.asyncio
async def test_get_brands_in_database():
    result = await service.get_all_brands()
    assert isinstance(result, list)


@pytest.mark.asyncio
async def test_delete_brands():
    name_1 = "Adidas"
    name_2 = "Zoom"

    result_true = await service.delete_brands(name_1)
    result_fake = await service.delete_brands(name_2)

    assert result_true is True
    assert result_fake is False
