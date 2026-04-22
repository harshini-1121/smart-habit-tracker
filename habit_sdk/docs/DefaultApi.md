# openapi_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_habit_habits_post**](DefaultApi.md#add_habit_habits_post) | **POST** /habits/ | Add Habit
[**create_user_users_post**](DefaultApi.md#create_user_users_post) | **POST** /users/ | Create User
[**log_habit_habits_id_log_patch**](DefaultApi.md#log_habit_habits_id_log_patch) | **PATCH** /habits/{id}/log | Log Habit
[**login_token_post**](DefaultApi.md#login_token_post) | **POST** /token | Login
[**read_habits_habits_get**](DefaultApi.md#read_habits_habits_get) | **GET** /habits/ | Read Habits


# **add_habit_habits_post**
> Habit add_habit_habits_post(habit_create)

Add Habit

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
    api_instance = openapi_client.DefaultApi(api_client)
    habit_create = openapi_client.HabitCreate() # HabitCreate | 

    try:
        # Add Habit
        api_response = api_instance.add_habit_habits_post(habit_create)
        print("The response of DefaultApi->add_habit_habits_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->add_habit_habits_post: %s\n" % e)
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

# **create_user_users_post**
> UserCreate create_user_users_post(user_create)

Create User

### Example


```python
import openapi_client
from openapi_client.models.user_create import UserCreate
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    user_create = openapi_client.UserCreate() # UserCreate | 

    try:
        # Create User
        api_response = api_instance.create_user_users_post(user_create)
        print("The response of DefaultApi->create_user_users_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_user_users_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_create** | [**UserCreate**](UserCreate.md)|  | 

### Return type

[**UserCreate**](UserCreate.md)

### Authorization

No authorization required

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

Log Habit

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
    api_instance = openapi_client.DefaultApi(api_client)
    id = 56 # int | 
    log_update = openapi_client.LogUpdate() # LogUpdate | 

    try:
        # Log Habit
        api_response = api_instance.log_habit_habits_id_log_patch(id, log_update)
        print("The response of DefaultApi->log_habit_habits_id_log_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->log_habit_habits_id_log_patch: %s\n" % e)
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

# **login_token_post**
> Token login_token_post(username, password, grant_type=grant_type, scope=scope, client_id=client_id, client_secret=client_secret)

Login

### Example


```python
import openapi_client
from openapi_client.models.token import Token
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    username = 'username_example' # str | 
    password = 'password_example' # str | 
    grant_type = 'grant_type_example' # str |  (optional)
    scope = '' # str |  (optional) (default to '')
    client_id = 'client_id_example' # str |  (optional)
    client_secret = 'client_secret_example' # str |  (optional)

    try:
        # Login
        api_response = api_instance.login_token_post(username, password, grant_type=grant_type, scope=scope, client_id=client_id, client_secret=client_secret)
        print("The response of DefaultApi->login_token_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->login_token_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **password** | **str**|  | 
 **grant_type** | **str**|  | [optional] 
 **scope** | **str**|  | [optional] [default to &#39;&#39;]
 **client_id** | **str**|  | [optional] 
 **client_secret** | **str**|  | [optional] 

### Return type

[**Token**](Token.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_habits_habits_get**
> List[Habit] read_habits_habits_get()

Read Habits

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
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Read Habits
        api_response = api_instance.read_habits_habits_get()
        print("The response of DefaultApi->read_habits_habits_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->read_habits_habits_get: %s\n" % e)
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

