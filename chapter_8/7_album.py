def make_album(artist, title, num_songs=None):
    """Builds dictionary describing music"""
    album_dic = {
        'artist' : artist.title(),
        'title' : title.title(),
    }
    if num_songs:
        album_dic['num_songs'] = num_songs
    return album_dic

album = make_album('motion city soundtrack', 'commit this to memory',
                   num_songs=10)
print(album)

album = make_album('florence + the machine', 'under heaven, over hell')
print(album)

album = make_album('oreskaband', 'hot number')
print(album)