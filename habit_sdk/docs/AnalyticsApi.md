# openapi_client.AnalyticsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_habit_history_habits_id_history_get**](AnalyticsApi.md#get_habit_history_habits_id_history_get) | **GET** /habits/{id}/history | Get Habit Activity History


# **get_habit_history_habits_id_history_get**
> List[LogResponse] get_habit_history_habits_id_history_get(id)

Get Habit Activity History

Returns a full history of logs for the GitHub-style contribution chart.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import openapi_client
from openapi_client.models.log_response import LogResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AnalyticsApi(api_client)
    id = 56 # int | 

    try:
        # Get Habit Activity History
        api_response = api_instance.get_habit_history_habits_id_history_get(id)
        print("The response of AnalyticsApi->get_habit_history_habits_id_history_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->get_habit_history_habits_id_history_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**List[LogResponse]**](LogResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

