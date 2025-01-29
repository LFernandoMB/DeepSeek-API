import requests

# API key from DeepSeek
api_key = "your_api_key_here"

# API Endpoint
url = "https://api.deepseek.com/v1/chat/completions"

# Header Request
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# Request body (adjust according to the model and desired parameters)
data = {
    "model": "deepseek-chat",  # Model
    "messages": [
        {"role": "user", "content": "Olá, como posso integrar a API da DeepSeek?"}
    ],
    "temperature": 0.7,  # Creativity parameter
    "max_tokens": 100    # Token limit in response
}

# Submit the request
response = requests.post(url, headers=headers, json=data)

# Check the response
if response.status_code == 200:
    result = response.json()
    print("Response from API:", result["choices"][0]["message"]["content"])
else:
    print("Error:", response.status_code, response.text)