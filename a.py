import json

var = '{"id": 30009574,"key": "8f6ea174098cb43316cd3c7779067747519f58b9","status": "successful","sandbox": True, ' \
      '"created_at": "2022-09-27T02:10:47Z",    "finished_at": "2022-09-27T02:10:53Z",    "source_file": {        ' \
      '"id": 134588966,        "name": "a1.m4a",        "size": 30055    },    "target_files": [        {            ' \
      '"id": 134588976,            "name": "a1.wav",            "size": 141390        }    ],    "target_format": ' \
      '"wav",    "credit_cost": 1} '
data = json.loads(var)
print(data)
