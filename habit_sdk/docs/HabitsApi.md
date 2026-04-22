# openapi_client.HabitsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_habit_habits_post**](HabitsApi.md#add_habit_habits_post) | **POST** /habits/ | Create New Habit
[**log_habit_habits_id_log_patch**](HabitsApi.md#log_habit_habits_id_log_patch) | **PATCH** /habits/{id}/log | Log Habit Completion
[**read_habits_habits_get**](HabitsApi.md#read_habits_habits_get) | **GET** /habits/ | Get All User Habits


# **add_habit_habits_post**
> Habit add_habit_habits_post(habit_create)

Create New Habit

Initializes a new habit and sets the starting streak to 0.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import openapi_client
from openapi_client.models.habit import Habit
from openapi_client.models.habit_create import HabitCreate
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
    api_instance = openapi_client.HabitsApi(api_client)
    habit_create = openapi_client.HabitCreate() # HabitCreate | 

    try:
        # Create New Habit
        api_response = api_instance.add_habit_habits_post(habit_create)
        print("The response of HabitsApi->add_habit_habits_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HabitsApi->add_habit_habits_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **habit_create** | [**HabitCreate**](HabitCreate.md)|  | 

### Return type

[**Habit**](Habit.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **log_habit_habits_id_log_patch**
> Habit log_habit_habits_id_log_patch(id, log_update)

Log Habit Completion

Marks a habit as 'done' or 'missed' for the current day.
- **Validation**: Only one log allowed per day.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import openapi_client
from openapi_client.models.habit import Habit
from openapi_client.models.log_update import LogUpdate
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
    api_instance = openapi_client.HabitsApi(api_client)
    id = 56 # int | 
    log_update = openapi_client.LogUpdate() # LogUpdate | 

    try:
        # Log Habit Completion
        api_response = api_instance.log_habit_habits_id_log_patch(id, log_update)
        print("The response of HabitsApi->log_habit_habits_id_log_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HabitsApi->log_habit_habits_id_log_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **log_update** | [**LogUpdate**](LogUpdate.md)|  | 

### Return type

[**Habit**](Habit.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_habits_habits_get**
> List[Habit] read_habits_habits_get()

Get All User Habits

Retrieves all habits for the logged-in user.
**Logic Trigger**: This endpoint automatically syncs missed days since the last login.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import openapi_client
from openapi_client.models.habit import Habit
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
    api_instance = openapi_client.HabitsApi(api_client)

    try:
        # Get All User Habits
        api_response = api_instance.read_habits_habits_get()
        print("The response of HabitsApi->read_habits_habits_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HabitsApi->read_habits_habits_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Habit]**](Habit.md)

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

