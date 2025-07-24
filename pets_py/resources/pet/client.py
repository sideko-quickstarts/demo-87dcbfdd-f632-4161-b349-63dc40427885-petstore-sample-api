import httpx
import typing
import typing_extensions

from pets_py.core import (
    AsyncBaseClient,
    BinaryResponse,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
    type_utils,
)
from pets_py.resources.pet.find_by_status import (
    AsyncFindByStatusClient,
    FindByStatusClient,
)
from pets_py.resources.pet.upload_image import AsyncUploadImageClient, UploadImageClient
from pets_py.types import models, params


class PetClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.find_by_status = FindByStatusClient(base_client=self._base_client)
        self.upload_image = UploadImageClient(base_client=self._base_client)

    def delete(
        self, *, pet_id: int, request_options: typing.Optional[RequestOptions] = None
    ) -> httpx.Response:
        """
        Deletes a pet.

        Delete a pet.

        DELETE /pet/{petId}

        Args:
            petId: Pet id to delete
            request_options: Additional options to customize the HTTP request

        Returns:
            Pet deleted

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.pet.delete(pet_id=123)
        ```
        """
        return self._base_client.request(
            method="DELETE",
            path=f"/pet/{pet_id}",
            auth_names=["api_key"],
            cast_to=httpx.Response,
            request_options=request_options or default_request_options(),
        )

    def get(
        self, *, pet_id: int, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Union[models.Pet, BinaryResponse]:
        """
        Find pet by ID.

        Returns a single pet.

        GET /pet/{petId}

        Args:
            petId: ID of pet to return
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.pet.get(pet_id=123)
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/pet/{pet_id}",
            auth_names=["api_key"],
            cast_to=typing.Union[models.Pet, BinaryResponse],
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        name: str,
        photo_urls: typing.List[str],
        category: typing.Union[
            typing.Optional[params.Category], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        id: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[typing_extensions.Literal["available", "pending", "sold"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        tags: typing.Union[
            typing.Optional[typing.List[params.Tag]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[models.Pet, BinaryResponse]:
        """
        Add a new pet to the store.

        Add a new pet to the store.

        POST /pet

        Args:
            category: Category
            id: int
            status: pet status in the store
            tags: typing.List[Tag]
            name: str
            photoUrls: typing.List[str]
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.pet.create(name="doggie", photo_urls=["string"], id=10)
        ```
        """
        _json = to_encodable(
            item={
                "category": category,
                "id": id,
                "status": status,
                "tags": tags,
                "name": name,
                "photo_urls": photo_urls,
            },
            dump_with=params._SerializerPet,
        )
        return self._base_client.request(
            method="POST",
            path="/pet",
            auth_names=["api_key"],
            json=_json,
            cast_to=typing.Union[models.Pet, BinaryResponse],
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        name: str,
        photo_urls: typing.List[str],
        category: typing.Union[
            typing.Optional[params.Category], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        id: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[typing_extensions.Literal["available", "pending", "sold"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        tags: typing.Union[
            typing.Optional[typing.List[params.Tag]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[models.Pet, BinaryResponse]:
        """
        Update an existing pet.

        Update an existing pet by Id.

        PUT /pet

        Args:
            category: Category
            id: int
            status: pet status in the store
            tags: typing.List[Tag]
            name: str
            photoUrls: typing.List[str]
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.pet.update(name="doggie", photo_urls=["string"], id=10)
        ```
        """
        _json = to_encodable(
            item={
                "category": category,
                "id": id,
                "status": status,
                "tags": tags,
                "name": name,
                "photo_urls": photo_urls,
            },
            dump_with=params._SerializerPet,
        )
        return self._base_client.request(
            method="PUT",
            path="/pet",
            auth_names=["api_key"],
            json=_json,
            cast_to=typing.Union[models.Pet, BinaryResponse],
            request_options=request_options or default_request_options(),
        )


class AsyncPetClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.find_by_status = AsyncFindByStatusClient(base_client=self._base_client)
        self.upload_image = AsyncUploadImageClient(base_client=self._base_client)

    async def delete(
        self, *, pet_id: int, request_options: typing.Optional[RequestOptions] = None
    ) -> httpx.Response:
        """
        Deletes a pet.

        Delete a pet.

        DELETE /pet/{petId}

        Args:
            petId: Pet id to delete
            request_options: Additional options to customize the HTTP request

        Returns:
            Pet deleted

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.pet.delete(pet_id=123)
        ```
        """
        return await self._base_client.request(
            method="DELETE",
            path=f"/pet/{pet_id}",
            auth_names=["api_key"],
            cast_to=httpx.Response,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self, *, pet_id: int, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Union[models.Pet, BinaryResponse]:
        """
        Find pet by ID.

        Returns a single pet.

        GET /pet/{petId}

        Args:
            petId: ID of pet to return
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.pet.get(pet_id=123)
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/pet/{pet_id}",
            auth_names=["api_key"],
            cast_to=typing.Union[models.Pet, BinaryResponse],
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        name: str,
        photo_urls: typing.List[str],
        category: typing.Union[
            typing.Optional[params.Category], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        id: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[typing_extensions.Literal["available", "pending", "sold"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        tags: typing.Union[
            typing.Optional[typing.List[params.Tag]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[models.Pet, BinaryResponse]:
        """
        Add a new pet to the store.

        Add a new pet to the store.

        POST /pet

        Args:
            category: Category
            id: int
            status: pet status in the store
            tags: typing.List[Tag]
            name: str
            photoUrls: typing.List[str]
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.pet.create(name="doggie", photo_urls=["string"], id=10)
        ```
        """
        _json = to_encodable(
            item={
                "category": category,
                "id": id,
                "status": status,
                "tags": tags,
                "name": name,
                "photo_urls": photo_urls,
            },
            dump_with=params._SerializerPet,
        )
        return await self._base_client.request(
            method="POST",
            path="/pet",
            auth_names=["api_key"],
            json=_json,
            cast_to=typing.Union[models.Pet, BinaryResponse],
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        name: str,
        photo_urls: typing.List[str],
        category: typing.Union[
            typing.Optional[params.Category], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        id: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[typing_extensions.Literal["available", "pending", "sold"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        tags: typing.Union[
            typing.Optional[typing.List[params.Tag]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[models.Pet, BinaryResponse]:
        """
        Update an existing pet.

        Update an existing pet by Id.

        PUT /pet

        Args:
            category: Category
            id: int
            status: pet status in the store
            tags: typing.List[Tag]
            name: str
            photoUrls: typing.List[str]
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.pet.update(name="doggie", photo_urls=["string"], id=10)
        ```
        """
        _json = to_encodable(
            item={
                "category": category,
                "id": id,
                "status": status,
                "tags": tags,
                "name": name,
                "photo_urls": photo_urls,
            },
            dump_with=params._SerializerPet,
        )
        return await self._base_client.request(
            method="PUT",
            path="/pet",
            auth_names=["api_key"],
            json=_json,
            cast_to=typing.Union[models.Pet, BinaryResponse],
            request_options=request_options or default_request_options(),
        )
