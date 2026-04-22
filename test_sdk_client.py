import openapi_client
from openapi_client.api.habits_api import HabitsApi
from openapi_client.api_client import ApiClient
from openapi_client.configuration import Configuration

# 1. Setup Configuration
# Note: The generator often adds /v1 or similar if not specified, 
# but FastAPI usually sits at the root.
config = Configuration(host="http://localhost:8000")
client = ApiClient(configuration=config)

# 2. Add your Token
# Replace this with a real token from your browser's LocalStorage
token = "eeyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0QGdtYWlsLmNvbSIsImV4cCI6MTc3Njc1MTU5NX0.O0aeuZJAAAmko77riqPqi4ici7Ii63-z6_vCUn-8Fbc"
client.set_default_header("Authorization", f"Bearer {token}")

# 3. Initialize the API
api_instance = HabitsApi(client)

try:
    # 4. Call the Get Habits method
    # The method name is usually 'read_habits_habits_get' based on FastAPI defaults
    habits = api_instance.read_habits_habits_get()
    
    print("--- Habits retrieved via Generated SDK ---")
    for habit in habits:
        print(f"Name: {habit.name} | Streak: {habit.streak} | Last Processed: {habit.last_processed_date}")
        
except openapi_client.ApiException as e:
    print(f"Exception when calling HabitsApi->read_habits: {e}")
except Exception as e:
    print(f"An error occurred: {e}")