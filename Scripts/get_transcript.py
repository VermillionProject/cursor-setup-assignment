from youtube_transcript_api import YouTubeTranscriptApi

video_id = "BJKAurmQ0zA"

transcript = YouTubeTranscriptApi().fetch(video_id)

for item in transcript:
    print(item.text)