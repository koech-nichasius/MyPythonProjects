"""This module contains data definitions for testing API."""
from typing import Any
from dataclasses import dataclass

@dataclass(frozen=True)
class StatusCodes:
    """This class defines API Test data."""
    OK: int = 200
    Created: int = 201
    Accepted: int = 202
    Deleted: int = 204



@dataclass(frozen=True)
class ApiTestData:
    """This class defines API Test data."""
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: None | str | dict[str, Any]

payload = {
  "name": "Nichasius",
  "job": "QA Engineer"}

valid_api_test_data = [
    ApiTestData(
        id=1,
        email="george.bluth@dotesthere.com",
        first_name="George",
        last_name="Bluth",
        avatar="https://dotesthere.com/img/faces/1-image.jpg")]
