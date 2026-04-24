from typing import Any, Dict


class ProductsAPI:
    """This class implements API wrapper for product-related endpoints.
    All operations related to products are encapsulated and HTTP communication delegated
    to the provided API client.
    """
    def __init__(self, client):
        """Initialize the productsAPI."""
        self.client = client

    def get_products(self, page: int = 1) -> Dict[str, Any]:
        """Retrieve a paginated list of products.
        Return response payload or status information from the get action"""
        return self.client.get("/products", params={"page": page})