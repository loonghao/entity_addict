from entity_addict import entity_addict


def test_dict():
    @entity_addict
    def get_dict_data_a():
        return {"key_name": "value"}

    assert get_dict_data_a().key_name == "value"


def test_list_of_dict():
    @entity_addict
    def get_dict_data_a():
        return [{"key_name": "value"}]

    assert get_dict_data_a()[0].key_name == "value"


def test_multi_list_of_dict():
    @entity_addict
    def get_dict_data_c():
        return [
            {"key_name": "value"},
            {"key": [{"sub_key1": 1}, {"sub_key2": 2}]},
        ]

    assert get_dict_data_c()[1].key[1].sub_key2 == 2
