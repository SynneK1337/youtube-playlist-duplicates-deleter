import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors


def main():
    scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]
    # Disable HTTPS Verification, don' t use this on production
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    API_SERVICE_NAME = "youtube"
    API_VERSION = "v3"
    CLIENT_SECRETS_FILENAME = "credentials.json"

    # Parse credentials from credentials.json file
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        CLIENT_SECRETS_FILENAME, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        API_SERVICE_NAME, API_VERSION, credentials=credentials
    )

    playlistId = input("Enter playlist URL: ")
    playlistId = playlistId.split('=')[1]
    items = get_playlist_items(youtube, playlistId)
    spotted_video_ids = []
    removed = 0
    for item in items:
        if item["snippet"]["resourceId"]["videoId"] not in spotted_video_ids:
            spotted_video_ids.append(item["snippet"]["resourceId"]["videoId"])
        else:
            delete_duplicate(youtube, item["id"])
            print(f"{item['snippet']['title']} removed.")
            removed += 1
    print(f"Removed {removed} items.")


def get_playlist_items(youtube, playlist_id):
    next_page_token = None
    items = []
    while next_page_token != "":
        request = youtube.playlistItems().list(
            part="snippet",
            maxResults=50,
            playlistId=playlist_id,
            pageToken=next_page_token
        )
        response = request.execute()
        try:
            next_page_token = response["nextPageToken"]
        except KeyError:
            next_page_token = ""
        for item in response["items"]:
            items.append(item)
    return items


def delete_duplicate(youtube, duplicate_id):
    youtube.playlistItems().delete(
        id=duplicate_id
    ).execute()


if __name__ == "__main__":
    main()
