entity_addict
=============
An extended version of [addict](https://github.com/mewwts/addict).

It can be very useful as a decorator. 
It can be converted to Dict when the function returns a value.
Can support a single dictionary, list dictionary, or multi deep  dictionary of list.

install via pip
```cmd
pip install entiry_addict
```

examples:
```python
from entity_addict import entity_addict
    
@entity_addict
def get_dict_data_a():
    return {"key_name": "value"}

data = get_dict_data_a()
print(data.key_name)

@entity_addict
def get_dict_data_b():
    return [{"key_name": "value"}]

for data in get_dict_data_b():
    print(data.key_name)

@entity_addict
def get_dict_data_c():
    return [
        {"key_name": "value"},
        {"key": [{"sub_key1": 1}, {"sub_key2": 2}]}
    ]
data = get_dict_data_c()
print(data[1].key[1].sub_key2)

```
