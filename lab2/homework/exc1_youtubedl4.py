from youtube_dl import YoutubeDL
options = {
    'default_search': 'ytsearch',
    'max_download': 1,
}
d1 = YoutubeDL(options)
d1.download(['pop/stars'])