Run `digester_server.py` to run a gRPC server.

In a separate window, fire up the python interpreter, and write the following:

```python
from digestor_client import DigestorClient
curr_client = DigestorClient()
```

Using the above client instance you can call the gRPC without doing any sort of network handling. Just call the get_digest function on the client object to invoke the gRPC. For example:

```python
curr_client.get_digest('Random12312312ascsafdaasdcsadcsds')
```

prints out the output

```
Digested: "060fe12e4eddf4acd8253cb508a9e58e95c04a24e07998808d86e76eaf942b15"
WasDigested: true
```

for streaming 

```python
curr_client.get_streaming_digest('This is a sample test where I get streaming responses')
```

prints out the output

```
ToDigest: "86e1de74820a9b252ba33b2eed445b0cd02c445b5f4b8007205aff1762d7301a"
ToDigest: "fa51fd49abf67705d6a35d18218c115ff5633aec1f9ebfdc9d5d4956416f57f6"
ToDigest: "ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb"
ToDigest: "af2bdbe1aa9b6ec1e2ade1d694f41fc71a831d0268e9891562113d8a62add1bf"
ToDigest: "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08"
ToDigest: "b48111c10c65fc119368edafb19f97451759ee90b3f44647368135ca47aa4753"
ToDigest: "a83dd0ccbffe39d071cc317ddf6e97f5c6b1c87af91919271f9fa140b0508c6c"
ToDigest: "2998b3232d29e8dc5a78d97a32ce83f556f3ed31b057077503df05641dd79158"
ToDigest: "b304adc33719d6cddb96d6c4f1aa46628d927547b49b70c981c7fea953e0600a"
ToDigest: "e30b3910ffd943c99f7edd7543c56c608522784ec521e85a91cf296f14a13e72"
```