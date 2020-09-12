entity_addict
=============
An extended version of addict.

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

```
