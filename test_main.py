from main import flatten


def test_flatten_no():
    assert flatten({"a": 1}) == [{"a": 1}]


def test_single_list():
    assert flatten({"a": [1, 2]}) == [{"a": 1}, {"a": 2}]


def test_parrallell_list():
    assert flatten({"a": [1, 2], "b": [3, 4]}) == [
        {"a": 1, "b": 3},
        {"a": 1, "b": 4},
        {"a": 2, "b": 3},
        {"a": 2, "b": 4},
    ]


def test_single_dict():
    assert flatten({"a": {"b": 1}}) == [{"a.b": 1}]


def test_parallell_dict():
    assert flatten({"a": {"b": 1, "c": 2}}) == [{"a.b": 1, "a.c": 2}]


def test_dict_nested():
    assert flatten({"a": 1, "b": {"c": 2, "d": {"e": 3, "f": [4, 5]}},}) == [
        {"a": 1, "b.c": 2, "b.d.e": 3, "b.d.f": 4},
        {"a": 1, "b.c": 2, "b.d.e": 3, "b.d.f": 5},
    ]


def test_flatten_complex():
    assert flatten(
        {
            "a": 1,
            "b": {
                "c": [{"d": 2}, {"e": 3}],
                "d": [{"e": 4}, {"f": 5}],
                "g": 6,
            },
        },
    ) == [
        {"a": 1, "b.c.d": 2, "b.d.e": 4, "b.g": 6},
        {"a": 1, "b.c.d": 2, "b.d.f": 5, "b.g": 6},
        {"a": 1, "b.c.e": 3, "b.d.e": 4, "b.g": 6},
        {"a": 1, "b.c.e": 3, "b.d.f": 5, "b.g": 6},
    ]
