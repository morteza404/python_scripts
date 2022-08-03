### Run the Server
```bash
python api.py
```

### make a get request:

```bash
curl http://localhost:5000/
{
    "hello": "world"
}
```
### make a post request:

```bash
curl -XPOST http://localhost:5000/ -d '{"firstname": "ruan", "lastname": "bekker"}'

{
  "firstname": "ruan",
  "lastname": "bekker"
}
```