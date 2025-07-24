
### Deletes a pet. <a name="delete"></a>

Delete a pet.

**API Endpoint**: `DELETE /pet/{petId}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `petId` | ✓ | Pet id to delete | `123` |

#### Synchronous Client

```python
from os import getenv
from pets_py import Client

client = Client(api_key=getenv("API_KEY"))
res = client.pet.delete(pet_id=123)

```

#### Asynchronous Client

```python
from os import getenv
from pets_py import AsyncClient

client = AsyncClient(api_key=getenv("API_KEY"))
res = await client.pet.delete(pet_id=123)

```

### Find pet by ID. <a name="get"></a>

Returns a single pet.

**API Endpoint**: `GET /pet/{petId}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `petId` | ✓ | ID of pet to return | `123` |

#### Synchronous Client

```python
from os import getenv
from pets_py import Client

client = Client(api_key=getenv("API_KEY"))
res = client.pet.get(pet_id=123)

```

#### Asynchronous Client

```python
from os import getenv
from pets_py import AsyncClient

client = AsyncClient(api_key=getenv("API_KEY"))
res = await client.pet.get(pet_id=123)

```

### Add a new pet to the store. <a name="create"></a>

Add a new pet to the store.

**API Endpoint**: `POST /pet`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `name` | ✓ |  | `"doggie"` |
| `photoUrls` | ✓ |  | `["string"]` |
| `category` | ✗ |  | `{"id": 1, "name": "Dogs"}` |
| `id` | ✗ |  | `10` |
| `status` | ✗ | pet status in the store | `"available"` |
| `tags` | ✗ |  | `[{}]` |

#### Synchronous Client

```python
from os import getenv
from pets_py import Client

client = Client(api_key=getenv("API_KEY"))
res = client.pet.create(name="doggie", photo_urls=["string"], id=10)

```

#### Asynchronous Client

```python
from os import getenv
from pets_py import AsyncClient

client = AsyncClient(api_key=getenv("API_KEY"))
res = await client.pet.create(name="doggie", photo_urls=["string"], id=10)

```

### Update an existing pet. <a name="update"></a>

Update an existing pet by Id.

**API Endpoint**: `PUT /pet`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `name` | ✓ |  | `"doggie"` |
| `photoUrls` | ✓ |  | `["string"]` |
| `category` | ✗ |  | `{"id": 1, "name": "Dogs"}` |
| `id` | ✗ |  | `10` |
| `status` | ✗ | pet status in the store | `"available"` |
| `tags` | ✗ |  | `[{}]` |

#### Synchronous Client

```python
from os import getenv
from pets_py import Client

client = Client(api_key=getenv("API_KEY"))
res = client.pet.update(name="doggie", photo_urls=["string"], id=10)

```

#### Asynchronous Client

```python
from os import getenv
from pets_py import AsyncClient

client = AsyncClient(api_key=getenv("API_KEY"))
res = await client.pet.update(name="doggie", photo_urls=["string"], id=10)

```
