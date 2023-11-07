Rajaongkir Py
=============================================


## How To Install
```commandline
pip install rajaongkir-py
```

## How To Run
```python
from rajaongkir_py.api import Rajaongkir
from rajaongkir_py.constants import ACCOUNT_STARTER

# ------------- initial -------------
api = Rajaongkir(
    key="my_secret",
    account_type=ACCOUNT_STARTER,
)

# ------------- Province -------------
api.get_provinces()
# api.get_provinces(id=1) # params

# results:
# [
#   {
#       "id": 1,
#       ....
#   },
#   { ... },
#    ...
# ]

api.get_province(id=1)
# api.get_province(
#   id=1, 
#   raise_error=False,
#   params={},
# )

# results:
# {
#     "id": 1,
#     ....
# }

# ------------- CITY -------------
api.get_cities()
# api.get_cities(id=1, province_id=1) # params

# results:
# [
#   {
#       "id": 1,
#       "province_id": 10,
#       ...
#   },
#   { ... },
#    ...
# ]

api.get_city(id=1)
# api.get_city(
#   id=1, 
#   raise_error=False,
#   params={'province_id': 21}
# )

# results:
# {
#     "id": 1,
#     ....
# }
```

## Contributors
* Agung Yuliyanto: [Github](https://github.com/agung96tm), [LinkedIn](https://www.linkedin.com/in/agung96tm/)
