# from googleapiclient.discovery import build

# # Set your API key here
# API_KEY = 'AIzaSyBCgCSY8JsEoRED4cTTjVzH1-WzdOK4vaQ'

# # Create a YouTube API client
# youtube = build('youtube', 'v3', developerKey='AIzaSyBCgCSY8JsEoRED4cTTjVzH1-WzdOK4vaQ')

# # Video ID of the video you want to retrieve info forpython your_script_name.py

# video_id = 'MBlWbsymDwc'

# # Call the videos().list method to retrieve video details
# video_request = youtube.videos().list(
#     part='snippet',
#     id=video_id
# )

# # Execute the request and get the response
# response = video_request.execute()

# # Print the video title and description
# if 'items' in response:
#     video = response['items'][0]
#     print('Video Title:', video['snippet']['title'])
#     print('Video Description:', video['snippet']['description'])
# else:
#     print('No video details found.')
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Set the API scopes for YouTube Data API
SCOPES = ["https://www.googleapis.com/auth/youtube.readonly"]

def get_authenticated_service():
    # Set up the OAuth 2.0 client flow
    flow = InstalledAppFlow.from_client_secrets_file(
        "C:\\Users\\HP\\Documents\\GitHub\Esya-HackCOG\\Datatube\\client_secret.json", SCOPES
    )
    
    # Run the flow to obtain credentials
    credentials = flow.run_local_server()

    # Create a YouTube Data API client
    youtube = build('youtube', 'v3', credentials=credentials)

    return youtube

if __name__ == "__main__":
    youtube = get_authenticated_service()

    # Specify the channel's username (e.g., YouTube's official channel)
    channel_username = "YouTube"

    # Get channel information
    response = youtube.channels().list(part="snippet", forUsername=channel_username).execute()

    # Print the channel information
    channel_info = response.get("items", [])
    if channel_info:
        print("Channel Title:", channel_info[0]["snippet"]["title"])
        print("Channel Description:", channel_info[0]["snippet"]["description"])
    else:
        print("Channel not found.")
