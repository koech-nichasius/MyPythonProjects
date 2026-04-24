from api_testing.api_data.api_test_data import StatusCodes
from api_testing.utils.assertions import assert_status_code


def test_get_products(products_api):
    """Test retrieve a single page of products."""
    response = products_api.get_products(page=1)
    assert_status_code(response=response, expected=StatusCodes.OK)
    data = response.json()
    assert "data" in data
    assert len(data["data"]) > 0