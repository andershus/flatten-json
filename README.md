# flatten-json
Flattens two different types of python objects in a dictionary:
## dict:

```python
flatten({"a": {"b": 1}}) == [{"a.b": 1}]
```
*Returns a list to be unified with the list case*

## list:

```python
flatten({"a": [1, 2]}) == [{"a": 1}, {"a": 2}]
```

## Expected application

To flatten a dictionaries where each element in a list has the same shape so it could fit in a table

```python
flatten(
    {
        "key": 123,
        "timesteps": [
            {"timestamp": 1, "value": 10}, 
            {"timestamp": 2, "value": 20}
        ]
    }
) == [
    {
        "key": 123, 
        "timesteps.timestamp": 1, 
        "timesteps.value": 10
    },
    {
        "key": 123, 
        "timesteps.timestamp": 2, 
        "timesteps.value": 20
    }
]
```