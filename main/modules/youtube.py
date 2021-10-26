from apiclient.discovery import build

#環境変数の設定（API_KEY, CHANNEL_ID）
import environ
env = environ.Env()
env.read_env('.env')

def get_youtube():
    API_KEY = env('API_KEY')
    YOUTUBE_API_SERVICE_NAME = 'youtube'
    YOUTUBE_API_VERSION = 'v3'
    CHANNEL_ID = env('CHANNEL_ID')
    searches = [] #videoidを格納する配列
    videos = [] #各動画情報を格納する配列

    youtube = build(
        YOUTUBE_API_SERVICE_NAME, 
        YOUTUBE_API_VERSION,
        developerKey=API_KEY
        )

    #動画情報取得
    search_response = youtube.search().list(
        part = "snippet",
        channelId = CHANNEL_ID,
        maxResults = 100,
        order = "date", 
        ).execute()
 
    #videoidの格納
    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            searches.append(search_result["id"]["videoId"])

    #各動画情報の格納
    for result in searches:
        video_response = youtube.videos().list(
        part = 'snippet,statistics',
        id = result
        ).execute()

        for video_result in video_response.get("items", []):
            if video_result["kind"] == "youtube#video":
                videos.append([video_result["snippet"]["publishedAt"],
                    video_result["snippet"]["title"],
                    result])
    return(videos)

