# pythontest
Basic RESTful API test skills
Runs on Flask

There are three endpoints:

- /getcode (methods:GET)
- /submitcode (methods:POST)
- /submitcode  (methods:POST)

sample response data from /getcode:
```
{"id": 9022, "sumvalue": 5, "values": [58, 36, 25, 83, 56, 68,...]}
```
acceptrable POST body data to /submitcode:
```
{"id": 9022, "answer": <youranswerhere>}
```



