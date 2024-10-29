import pytest
from app.bisnes_services.repository.sneaker_services import SneakerService
from app.bisnes_services.shemas.sneakers_shemas import SneakerFilterShemas
from app.bisnes_services.models.sneakers import Sneakers


@pytest.mark.asyncio
async def test_get_by_filter():
    sneaker_service = SneakerService()
    sneaker_mock_data_true = SneakerFilterShemas(
        name="Adidas", price_max=180, price_min=0
    )
    sneaker_mock_data_false = SneakerFilterShemas(
        name="akalwdj", price_max=18000, price_min=-200
    )
    result_1 = await sneaker_service.get_by_filter(sneaker_mock_data_true)
    result_2 = await sneaker_service.get_by_filter(sneaker_mock_data_false)
    assert isinstance(result_1, list)
    assert all(isinstance(sneaker, Sneakers) for sneaker in result_1)
    assert result_2 is False
