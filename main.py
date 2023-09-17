"""Flatten a nested json to one not containing and dicts or lists."""


def flatten(data: dict) -> list[dict[str, str | int | bool | None]]:
    """Flatten a nested dictionary."""
    if any(isinstance(value, list) for value in data.values()):
        for key, value in data.items():
            if isinstance(value, list):
                return sum([flatten(data | {key: item}) for item in value], [])
    if any(isinstance(value, dict) for value in data.values()):
        output = {}
        for key, value in data.items():
            if isinstance(value, dict):
                for subkey, subvalue in value.items():
                    output[key + "." + subkey] = subvalue
            else:
                output[key] = value
        return flatten(output)
    return [data]
