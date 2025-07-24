import httpx
import pydantic
import pytest

from pets_py import AsyncClient, Client
from pets_py.core import BinaryResponse
from pets_py.environment import Environment
from pets_py.types import models


def test_update_200_success_all_params():
    """Tests a PUT request to the /pet endpoint.

    Operation: update
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : typing.Union[models.Pet, BinaryResponse]

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_KEY", environment=Environment.MOCK_SERVER)
    response = client.pet.update(
        name="doggie",
        photo_urls=["string"],
        category={"id": 1, "name": "Dogs"},
        id=10,
        status="available",
        tags=[{"id": 123, "name": "string"}],
    )
    try:
        pydantic.TypeAdapter(models.Pet).validate_python(response)
        is_valid_response_json = True
    except pydantic.ValidationError:
        is_valid_response_json = False
    is_valid_binary = isinstance(response, BinaryResponse)
    assert any([is_valid_response_json, is_valid_binary]), "failed response type check"


@pytest.mark.asyncio
async def test_await_update_200_success_all_params():
    """Tests a PUT request to the /pet endpoint.

    Operation: update
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : typing.Union[models.Pet, BinaryResponse]

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_KEY", environment=Environment.MOCK_SERVER)
    response = await client.pet.update(
        name="doggie",
        photo_urls=["string"],
        category={"id": 1, "name": "Dogs"},
        id=10,
        status="available",
        tags=[{"id": 123, "name": "string"}],
    )
    try:
        pydantic.TypeAdapter(models.Pet).validate_python(response)
        is_valid_response_json = True
    except pydantic.ValidationError:
        is_valid_response_json = False
    is_valid_binary = isinstance(response, BinaryResponse)
    assert any([is_valid_response_json, is_valid_binary]), "failed response type check"


def test_create_200_success_all_params():
    """Tests a POST request to the /pet endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : typing.Union[models.Pet, BinaryResponse]

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_KEY", environment=Environment.MOCK_SERVER)
    response = client.pet.create(
        name="doggie",
        photo_urls=["string"],
        category={"id": 1, "name": "Dogs"},
        id=10,
        status="available",
        tags=[{"id": 123, "name": "string"}],
    )
    try:
        pydantic.TypeAdapter(models.Pet).validate_python(response)
        is_valid_response_json = True
    except pydantic.ValidationError:
        is_valid_response_json = False
    is_valid_binary = isinstance(response, BinaryResponse)
    assert any([is_valid_response_json, is_valid_binary]), "failed response type check"


@pytest.mark.asyncio
async def test_await_create_200_success_all_params():
    """Tests a POST request to the /pet endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : typing.Union[models.Pet, BinaryResponse]

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_KEY", environment=Environment.MOCK_SERVER)
    response = await client.pet.create(
        name="doggie",
        photo_urls=["string"],
        category={"id": 1, "name": "Dogs"},
        id=10,
        status="available",
        tags=[{"id": 123, "name": "string"}],
    )
    try:
        pydantic.TypeAdapter(models.Pet).validate_python(response)
        is_valid_response_json = True
    except pydantic.ValidationError:
        is_valid_response_json = False
    is_valid_binary = isinstance(response, BinaryResponse)
    assert any([is_valid_response_json, is_valid_binary]), "failed response type check"


def test_get_200_success_all_params():
    """Tests a GET request to the /pet/{petId} endpoint.

    Operation: get
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : typing.Union[models.Pet, BinaryResponse]

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_KEY", environment=Environment.MOCK_SERVER)
    response = client.pet.get(pet_id=123)
    try:
        pydantic.TypeAdapter(models.Pet).validate_python(response)
        is_valid_response_json = True
    except pydantic.ValidationError:
        is_valid_response_json = False
    is_valid_binary = isinstance(response, BinaryResponse)
    assert any([is_valid_response_json, is_valid_binary]), "failed response type check"


@pytest.mark.asyncio
async def test_await_get_200_success_all_params():
    """Tests a GET request to the /pet/{petId} endpoint.

    Operation: get
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : typing.Union[models.Pet, BinaryResponse]

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_KEY", environment=Environment.MOCK_SERVER)
    response = await client.pet.get(pet_id=123)
    try:
        pydantic.TypeAdapter(models.Pet).validate_python(response)
        is_valid_response_json = True
    except pydantic.ValidationError:
        is_valid_response_json = False
    is_valid_binary = isinstance(response, BinaryResponse)
    assert any([is_valid_response_json, is_valid_binary]), "failed response type check"


def test_delete_200_success_all_params():
    """Tests a DELETE request to the /pet/{petId} endpoint.

    Operation: delete
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : httpx.Response

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_KEY", environment=Environment.MOCK_SERVER)
    response = client.pet.delete(pet_id=123)
    assert isinstance(response, httpx.Response)


@pytest.mark.asyncio
async def test_await_delete_200_success_all_params():
    """Tests a DELETE request to the /pet/{petId} endpoint.

    Operation: delete
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : httpx.Response

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_KEY", environment=Environment.MOCK_SERVER)
    response = await client.pet.delete(pet_id=123)
    assert isinstance(response, httpx.Response)
