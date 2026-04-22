# LogResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**habit_id** | **int** |  | 
**var_date** | **date** |  | 
**status** | **str** |  | 

## Example

```python
from openapi_client.models.log_response import LogResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LogResponse from a JSON string
log_response_instance = LogResponse.from_json(json)
# print the JSON string representation of the object
print(LogResponse.to_json())

# convert the object into a dict
log_response_dict = log_response_instance.to_dict()
# create an instance of LogResponse from a dict
log_response_from_dict = LogResponse.from_dict(log_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


