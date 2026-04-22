# Habit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**id** | **int** |  | 
**streak** | **int** |  | 
**last_processed_date** | **date** |  | 

## Example

```python
from openapi_client.models.habit import Habit

# TODO update the JSON string below
json = "{}"
# create an instance of Habit from a JSON string
habit_instance = Habit.from_json(json)
# print the JSON string representation of the object
print(Habit.to_json())

# convert the object into a dict
habit_dict = habit_instance.to_dict()
# create an instance of Habit from a dict
habit_from_dict = Habit.from_dict(habit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


