# openapi_client.SimulationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**debug_reset_habits_id_debug_reset_post**](SimulationApi.md#debug_reset_habits_id_debug_reset_post) | **POST** /habits/{id}/debug-reset | Reset Today&#39;s Log
[**trigger_gap_habits_id_simulate_gap_post**](SimulationApi.md#trigger_gap_habits_id_simulate_gap_post) | **POST** /habits/{id}/simulate-gap | Simulate 3-Day Absence
[**trigger_reminder_habits_simulate_reminder_post**](SimulationApi.md#trigger_reminder_habits_simulate_reminder_post) | **POST** /habits/simulate-reminder | Simulate End-of-Day Email


# **debug_reset_habits_id_debug_reset_post**
> object debug_reset_habits_id_debug_reset_post(id)

Reset Today's Log

Deletes today's log entry so you can re-test the Done/Miss buttons.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import openapi_client
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
    api_instance = openapi_client.SimulationApi(api_client)
    id = 56 # int | 

    try:
        # Reset Today's Log
        api_response = api_instance.debug_reset_habits_id_debug_reset_post(id)
        print("The response of SimulationApi->debug_reset_habits_id_debug_reset_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SimulationApi->debug_reset_habits_id_debug_reset_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**object**

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

# **trigger_gap_habits_id_simulate_gap_post**
> object trigger_gap_habits_id_simulate_gap_post(id)

Simulate 3-Day Absence

Forces a date-gap in the DB. Refresh the habit list after calling this to trigger escalation.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import openapi_client
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
    api_instance = openapi_client.SimulationApi(api_client)
    id = 56 # int | 

    try:
        # Simulate 3-Day Absence
        api_response = api_instance.trigger_gap_habits_id_simulate_gap_post(id)
        print("The response of SimulationApi->trigger_gap_habits_id_simulate_gap_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SimulationApi->trigger_gap_habits_id_simulate_gap_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**object**

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

# **trigger_reminder_habits_simulate_reminder_post**
> object trigger_reminder_habits_simulate_reminder_post()

Simulate End-of-Day Email

Triggers the terminal output for habits not yet completed today.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import openapi_client
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
    api_instance = openapi_client.SimulationApi(api_client)

    try:
        # Simulate End-of-Day Email
        api_response = api_instance.trigger_reminder_habits_simulate_reminder_post()
        print("The response of SimulationApi->trigger_reminder_habits_simulate_reminder_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SimulationApi->trigger_reminder_habits_simulate_reminder_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

