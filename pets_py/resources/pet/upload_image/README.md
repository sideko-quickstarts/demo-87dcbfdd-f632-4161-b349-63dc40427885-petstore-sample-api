
### Uploads an image. <a name="create"></a>

Upload image of the pet.

**API Endpoint**: `POST /pet/{petId}/uploadImage`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `data` | ✓ |  | `open("uploads/file.pdf", "rb")` |
| `petId` | ✓ | ID of pet to update | `123` |
| `additionalMetadata` | ✗ | Additional Metadata | `"string"` |

#### Synchronous Client

```python
from os import getenv
from pets_py import Client

client = Client(api_key=getenv("API_KEY"))
res = client.pet.upload_image.create(data=open("uploads/file.pdf", "rb"), pet_id=123)

```

#### Asynchronous Client

```python
from os import getenv
from pets_py import AsyncClient

client = AsyncClient(api_key=getenv("API_KEY"))
res = await client.pet.upload_image.create(
    data=open("uploads/file.pdf", "rb"), pet_id=123
)

```

#### Response

##### Type
[ApiResponse](/pets_py/types/models/api_response.py)

##### Example
`{}`
