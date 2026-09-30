import yt_dlp

def telecharger_audio(url_youtube):
    options = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    
    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([url_youtube])

url = 'https://www.youtube.com/watch?v=tQOw_R2gx2E&list=RDtQOw_R2gx2E&start_radio=1'
telecharger_audio(url)
