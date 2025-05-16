from youtube_transcript_api import YouTubeTranscriptApi

video_id = 'YbJOTdZBX1g'  # Example video ID (isko change kar sakte ho)

try:
    transcript = YouTubeTranscriptApi.get_transcript(video_id)

    for item in transcript:
        print(item['text'])

except Exception as e:
    print("Error aaya hai:", e)
