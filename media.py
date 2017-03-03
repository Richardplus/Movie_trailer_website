class Movie():
    '''this class stores movie informations including movie title, box art URL (or poster URL) and a YouTube link to the movie trailer'''
    def __init__(self, title, poster_url, youtube_link):
        self.title = title
        self.poster_image_url = poster_url
        self.trailer_youtube_url = youtube_link
