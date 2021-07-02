from youtube_transcript_api import YouTubeTranscriptApi
def get_ytdata(id):
    transcript_list = YouTubeTranscriptApi.get_transcript(id)
    full_transcript = ""
    for transcript in transcript_list:
        timestamp = transcript['text'].split()
        full_transcript+=" "+" ".join(timestamp)
    return full_transcript