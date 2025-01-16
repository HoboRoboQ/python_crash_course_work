def make_album(artist, title):
    """Builds dictionary describing music"""
    album_dic = {
        'artist' : artist.title(),
        'title' : title.title(),
    }
    return album_dic