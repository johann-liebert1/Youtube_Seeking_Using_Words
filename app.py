import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(video_id, languages=['hi', 'en']):
    try:
        # Try to get the transcript in Hindi ('hi'), fallback to English ('en')
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=languages)
        return transcript
    except Exception as e:
        return None

def search_word_in_transcript(transcript, word):
    timestamps = []
    for entry in transcript:
        if word.lower() in entry['text'].lower():
            timestamps.append((entry['start'], entry['text']))
    return timestamps

def create_youtube_link(video_id, timestamp):
    return f"https://www.youtube.com/watch?v={video_id}&t={int(timestamp)}s"

def main():
    st.title("YouTube Transcript Searcher (Supports Hindi)")
    
    # Text area for multiple YouTube URLs
    video_urls = st.text_area("Enter YouTube Video URLs (one per line)")
    search_word = st.text_input("Enter the word to search (in Hindi or English)")
    
    if st.button("Search"):
        video_url_list = video_urls.splitlines()
        
        if not video_url_list:
            st.write("Please enter at least one YouTube URL.")
            return
        
        for video_url in video_url_list:
            video_id = video_url.split("v=")[-1]
            transcript = get_transcript(video_id)
            st.write(f"### Results for {video_url}")
            
            if transcript:
                timestamps = search_word_in_transcript(transcript, search_word)
                if timestamps:
                    for ts, text in timestamps:
                        link = create_youtube_link(video_id, ts)
                        st.write(f"[{text}]({link})")
                else:
                    st.write("Word not found in transcript.")
            else:
                st.write("Transcript not available.")
            st.write("---")  # Separator between results for different videos

if __name__ == "__main__":
    main()



# import streamlit as st
# from youtube_transcript_api import YouTubeTranscriptApi

# def get_transcript(video_id):
#     # Fetch transcript using YouTube Transcript API
#     try:
#         transcript = YouTubeTranscriptApi.get_transcript(video_id)
#         return transcript
#     except Exception as e:
#         return None

# def search_word_in_transcript(transcript, word):
#     # Search for the word in the transcript
#     timestamps = []
#     for entry in transcript:
#         if word.lower() in entry['text'].lower():
#             timestamps.append((entry['start'], entry['text']))
#     return timestamps

# def create_youtube_link(video_id, timestamp):
#     # Generate YouTube link with seek
#     return f"https://www.youtube.com/watch?v={video_id}&t={int(timestamp)}s"

# def main():
#     st.title("YouTube Transcript Searcher")
    
#     video_urls = st.text_area("Enter YouTube Video URLs (one per line)")
#     search_word = st.text_input("Enter the word to search")
    
#     if st.button("Search"):
#         video_url_list = video_urls.splitlines()
        
#         if not video_url_list:
#             st.write("Please enter at least one YouTube URL.")
#             return
        
#         for video_url in video_url_list:
#             video_id = video_url.split("v=")[-1]
#             transcript = get_transcript(video_id)
#             st.write(f"### Results for {video_url}")
            
#             if transcript:
#                 timestamps = search_word_in_transcript(transcript, search_word)
#                 if timestamps:
#                     for ts, text in timestamps:
#                         link = create_youtube_link(video_id, ts)
#                         st.write(f"[{text}]({link})")
#                 else:
#                     st.write("Word not found in transcript.")
#             else:
#                 st.write("Transcript not available.")
#             st.write("---")  

# if __name__ == "__main__":
#     main()