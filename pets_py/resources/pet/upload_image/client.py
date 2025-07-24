import httpx
import typing

from pets_py.core import (
    AsyncBaseClient,
    QueryParams,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    encode_query_param,
    to_content,
    to_encodable,
    type_utils,
)
from pets_py.types import models


class UploadImageClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create(
        self,
        *,
        data: httpx._types.FileTypes,
        pet_id: int,
        additional_metadata: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ApiResponse:
        """
        Uploads an image.

        Upload image of the pet.

        POST /pet/{petId}/uploadImage

        Args:
            additionalMetadata: Additional Metadata
            data: httpx._types.FileTypes
            petId: ID of pet to update
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.pet.upload_image.create(data=open("uploads/file.pdf", "rb"), pet_id=123)
        ```
        """
        _query: QueryParams = {}
        if not isinstance(additional_metadata, type_utils.NotGiven):
            encode_query_param(
                _query,
                "additionalMetadata",
                to_encodable(item=additional_metadata, dump_with=str),
                style="form",
                explode=True,
            )
        _content = to_content(file=data)
        _content_type = "application/octet-stream"
        return self._base_client.request(
            method="POST",
            path=f"/pet/{pet_id}/uploadImage",
            auth_names=["api_key"],
            query_params=_query,
            content=_content,
            content_type=_content_type,
            cast_to=models.ApiResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncUploadImageClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
        self,
        *,
        data: httpx._types.FileTypes,
        pet_id: int,
        additional_metadata: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ApiResponse:
        """
        Uploads an image.

        Upload image of the pet.

        POST /pet/{petId}/uploadImage

        Args:
            additionalMetadata: Additional Metadata
            data: httpx._types.FileTypes
            petId: ID of pet to update
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.pet.upload_image.create(
            data=open("uploads/file.pdf", "rb"), pet_id=123
        )
        ```
        """
        _query: QueryParams = {}
        if not isinstance(additional_metadata, type_utils.NotGiven):
            encode_query_param(
                _query,
                "additionalMetadata",
                to_encodable(item=additional_metadata, dump_with=str),
                style="form",
                explode=True,
            )
        _content = to_content(file=data)
        _content_type = "application/octet-stream"
        return await self._base_client.request(
            method="POST",
            path=f"/pet/{pet_id}/uploadImage",
            auth_names=["api_key"],
            query_params=_query,
            content=_content,
            content_type=_content_type,
            cast_to=models.ApiResponse,
            request_options=request_options or default_request_options(),
        )
