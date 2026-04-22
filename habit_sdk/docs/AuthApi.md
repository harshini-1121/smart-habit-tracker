# openapi_client.AuthApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user_users_post**](AuthApi.md#create_user_users_post) | **POST** /users/ | Register New User
[**login_token_post**](AuthApi.md#login_token_post) | **POST** /token | Login for Access Token


# **create_user_users_post**
> UserResponse create_user_users_post(user_create)

Register New User

Creates a new user profile and hashes the password.

### Example


```python
import openapi_client
from openapi_client.models.user_create import UserCreate
from openapi_client.models.user_response import UserResponse
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
    api_instance = openapi_client.AuthApi(api_client)
    user_create = openapi_client.UserCreate() # UserCreate | 

    try:
        # Register New User
        api_response = api_instance.create_user_users_post(user_create)
        print("The response of AuthApi->create_user_users_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->create_user_users_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_create** | [**UserCreate**](UserCreate.md)|  | 

### Return type

[**UserResponse**](UserResponse.md)

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

# **login_token_post**
> Token login_token_post(username, password, grant_type=grant_type, scope=scope, client_id=client_id, client_secret=client_secret)

Login for Access Token

Exchanges user credentials for a JWT Access Token.
- **username**: User's email
- **password**: User's plain-text password

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
    api_instance = openapi_client.AuthApi(api_client)
    username = 'username_example' # str | 
    password = 'password_example' # str | 
    grant_type = 'grant_type_example' # str |  (optional)
    scope = '' # str |  (optional) (default to '')
    client_id = 'client_id_example' # str |  (optional)
    client_secret = 'client_secret_example' # str |  (optional)

    try:
        # Login for Access Token
        api_response = api_instance.login_token_post(username, password, grant_type=grant_type, scope=scope, client_id=client_id, client_secret=client_secret)
        print("The response of AuthApi->login_token_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->login_token_post: %s\n" % e)
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

