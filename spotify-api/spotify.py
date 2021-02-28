import requests

CLIENT_ID = '8f764dab3e3c487a8f92cd678ab0d5e3'
CLIENT_SECRET = '6196612059d94e0eac212a74c50add4a'

AUTH_URL = 'https://accounts.spotify.com/api/token'

# POST
auth_response = requests.post(AUTH_URL, {
    'grant_type' : 'client_credentaiials',
    'client_id' : CLIENT_ID,
    'client_secret' : CLIENT_ID,
})

# convert the response to JSON
auth_response_data = auth_response.json()

# save the access token
access_token = auth_response_data['access_token']

