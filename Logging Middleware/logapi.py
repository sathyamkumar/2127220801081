import requests

def log_api(message:str):
    """
    Sends a log message to a remote logging server.
    
    Args:
        message (str): The log message to send.
    """
    url = "http://20.244.56.144/evaluation-service/log"
    headers = {"Content-Type": "application/json",'Authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiYXVkIjoiaHR0cDovLzIwLjI0NC41Ni4xNDQvZXZhbHVhdGlvbi1zZXJ2aWNlIiwiZW1haWwiOiIyMDIyaXQwMjIxQHN2Y2UuYWMuaW4iLCJleHAiOjE3NTE4NzYyMzksImlhdCI6MTc1MTg3NTMzOSwiaXNzIjoiQWZmb3JkIE1lZGljYWwgVGVjaG5vbG9naWVzIFByaXZhdGUgTGltaXRlZCIsImp0aSI6ImQ4MDRhOThhLTc4OGQtNGIzYS05ZDJlLWY0MjBhZjcxYzQ1YSIsImxvY2FsZSI6ImVuLUlOIiwibmFtZSI6InNhdGh5YW0ga3VtYXIgciIsInN1YiI6IjkxODA3NjQ5LTI2YzctNDdmYy04MzRmLWNlODMwNjA4YjM0OSJ9LCJlbWFpbCI6IjIwMjJpdDAyMjFAc3ZjZS5hYy5pbiIsIm5hbWUiOiJzYXRoeWFtIGt1bWFyIHIiLCJyb2xsTm8iOiIyMTI3MjIwODAxMDgxIiwiYWNjZXNzQ29kZSI6IlpSc1lYeCIsImNsaWVudElEIjoiOTE4MDc2NDktMjZjNy00N2ZjLTgzNGYtY2U4MzA2MDhiMzQ5IiwiY2xpZW50U2VjcmV0IjoibXhodFBuZEpkbXhSc0hFUyJ9.jsFPFed4KZs-6Wmet6nz5hjy3uK_YHJbyK2fQgy4W2k'}
    payload = {"message": message}
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to send log message: {e}")