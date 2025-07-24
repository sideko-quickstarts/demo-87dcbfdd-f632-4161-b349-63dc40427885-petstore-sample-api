
### Finds Pets by status. <a name="list"></a>

Multiple status values can be provided with comma separated strings.

**API Endpoint**: `GET /pet/findByStatus`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `status` | ✗ | Status values that need to be considered for filter | `"available"` |

#### Synchronous Client

```python
from os import getenv
from pets_py import Client

client = Client(api_key=getenv("API_KEY"))
res = client.pet.find_by_status.list()

```

#### Asynchronous Client

```python
from os import getenv
from pets_py import AsyncClient

client = AsyncClient(api_key=getenv("API_KEY"))
res = await client.pet.find_by_status.list()

```
