<p align="center">
<a href="https://img.shields.io/pypi/pyversions/entity_addict">
<img src="https://img.shields.io/pypi/pyversions/entity_addict" alt="python version"></a>
<a href="https://badge.fury.io/py/entity_addict">
<img src="https://img.shields.io/pypi/dw/entity_addict" alt="PyPI version"></a>
<a href="https://entity_addict.readthedocs.io/en/master/?badge=master">
<img src="https://img.shields.io/pypi/dw/entity_addict" alt="Downloads Status"></a>
<a href="https://pepy.tech/badge/entity_addict">
<img src="https://pepy.tech/badge/entity_addict" alt="Downloads"></a>
<img src="https://img.shields.io/pypi/l/entity_addict" alt="License"></a>
<img src="https://img.shields.io/pypi/format/entity_addict" alt="pypi format"></a>
<a href="https://discord.gg/AnxSa6n">
<a href="https://github.com/loonghao/entity_addict/graphs/commit-activity">
<img src="https://img.shields.io/badge/Maintained%3F-yes-green.svg" alt="Maintenance"></a>

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
