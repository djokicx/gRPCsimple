Run `digester_server.py` to run a gRPC server.

In a separate window, fire up the python interpreter, and write the following:

```python
from digestor_client import DigestorClient
curr_client = DigestorClient()
```

Using the above client instance you can call the gRPC without doing any sort of network handling. Just call the get_digest function on the client object to invoke the gRPC. For example:

```python
currs.curr_client('Random12312312ascsafdaasdcsadcsds')
```

prints out the output

```
Digested: "Random12312312ascsafdaasdcsadcsds"
WasDigested: true
```