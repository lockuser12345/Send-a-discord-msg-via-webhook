# do pip install requests 



import requests
import json

# Your webhook url
webhook_url = 'YOUR_WEBHOOK_URL'

# What you want to send
message = {
    'content': 'Your message here'
}


try:
    response = requests.post(webhook_url, data=json.dumps(message), headers={'Content-Type': 'application/json'})

    
    if response.status_code == 200:
        print('Message sent successfully')
    else:
        print(f'Failed to send message. Status code: {response.status_code}')

except requests.exceptions.RequestException as e:
    print(f'Error: {e}')
