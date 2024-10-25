import pytest
from app.bisnes_services.repository.sneaker_services import SneakerService


@pytest.mark.asyncio
async def test_get_by_filter():
    test_data = {"name": "Adidas", "price_min": 0, "price_max": 180}
    sneaker_service = SneakerService()
    result = sneaker_service.get_by_filter(test_data)
