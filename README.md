# PyVectorDB

PyVectorDB is a Python client library for working with the VectorDB database server. It provides a simple API for creating, reading, updating, and deleting vector data, as well as searching for similar vectors.

## Installation

You can install PyVectorDB using pip:
```bash
pip install git+https://www.github.com/rubythalib33/pyvectordb
```


## Usage

Here's an example of how to use the `VectorDBClient` class:

```python
from pyvectordb import VectorDBClient

# Create a new client instance
client = VectorDBClient('localhost', 8000)

# Authenticate with the server
client.auth('root', 'root')

# Create some data
client.create('label', [1.0, 2.0, 3.0])

# Read the data
data = client.read('label')
print(data)

# Update the data
client.update('label', [4.0, 5.0, 6.0])

# Search for similar data
similar_labels = client.search([4.0, 5.0, 6.0], 0.5, 1)
print(similar_labels)

# Delete the data
client.delete('label')

# Close the client connection
client.close()
```

## VectorDB Server
PyVectorDB requires a VectorDB server to be running in order to work. You can find a simple VectorDB server implementation in the [VectorDB repository](https://github.com/rubythalib33/VectorDB). The server uses Boost Asio for handling TCP connections.

## License
PyVectorDB is licensed under the MIT license. See the [LICENSE](LICENSE) file for details.