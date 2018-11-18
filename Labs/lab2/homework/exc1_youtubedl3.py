from youtube_dl import YoutubeDL
options = {
    'format': 'bestaudio/audio'
}
d1 = YoutubeDL(options)
d1.download(['https://www.youtube.com/watch?v=hUxFyYRPYuM'])