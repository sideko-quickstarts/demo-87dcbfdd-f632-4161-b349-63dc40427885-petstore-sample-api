import pydantic
import pytest
import typing

from pets_py import AsyncClient, Client
from pets_py.core import BinaryResponse
from pets_py.environment import Environment
from pets_py.types import models


def test_list_200_success_required_only():
    """Tests a GET request to the /pet/findByStatus endpoint.

    Operation: list
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Synchronous execution

    Response : typing.Union[typing.List[models.Pet], BinaryResponse]

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_KEY", environment=Environment.MOCK_SERVER)
    response = client.pet.find_by_status.list()
    try:
        pydantic.TypeAdapter(typing.List[models.Pet]).validate_python(response)
        is_valid_response_json = True
    except pydantic.ValidationError:
        is_valid_response_json = False
    is_valid_binary = isinstance(response, BinaryResponse)
    assert any([is_valid_response_json, is_valid_binary]), "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_success_required_only():
    """Tests a GET request to the /pet/findByStatus endpoint.

    Operation: list
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Asynchronous execution

    Response : typing.Union[typing.List[models.Pet], BinaryResponse]

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_KEY", environment=Environment.MOCK_SERVER)
    response = await client.pet.find_by_status.list()
    try:
        pydantic.TypeAdapter(typing.List[models.Pet]).validate_python(response)
        is_valid_response_json = True
    except pydantic.ValidationError:
        is_valid_response_json = False
    is_valid_binary = isinstance(response, BinaryResponse)
    assert any([is_valid_response_json, is_valid_binary]), "failed response type check"


def test_list_200_success_all_params():
    """Tests a GET request to the /pet/findByStatus endpoint.

    Operation: list
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : typing.Union[typing.List[models.Pet], BinaryResponse]

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_KEY", environment=Environment.MOCK_SERVER)
    response = client.pet.find_by_status.list(status="available")
    try:
        pydantic.TypeAdapter(typing.List[models.Pet]).validate_python(response)
        is_valid_response_json = True
    except pydantic.ValidationError:
        is_valid_response_json = False
    is_valid_binary = isinstance(response, BinaryResponse)
    assert any([is_valid_response_json, is_valid_binary]), "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_success_all_params():
    """Tests a GET request to the /pet/findByStatus endpoint.

    Operation: list
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : typing.Union[typing.List[models.Pet], BinaryResponse]

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_KEY", environment=Environment.MOCK_SERVER)
    response = await client.pet.find_by_status.list(status="available")
    try:
        pydantic.TypeAdapter(typing.List[models.Pet]).validate_python(response)
        is_valid_response_json = True
    except pydantic.ValidationError:
        is_valid_response_json = False
    is_valid_binary = isinstance(response, BinaryResponse)
    assert any([is_valid_response_json, is_valid_binary]), "failed response type check"
