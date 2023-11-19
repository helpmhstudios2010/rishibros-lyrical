
def get_lyrics(name:str,artists:list) -> str:
    import lyricsgenius as lg
    genius = lg.Genius("iJW_z3C4VVsgvOqjjHqcxBOdpm_zbzR-4sRZrebCxghL8HeI0gCcITND0nwyxGJu")
    artist_str = ",".join(artists)
    song = genius.search_song(name,artist_str)
    if song == None:
        return (f"Sorry, {name} by {artist_str} was not found")
    else:
        return _clean_lyrics(song.lyrics)


def _clean_lyrics(lyrics:str):
    import re
    lyrics = (re.sub(r"\[.*?\]","",lyrics))
    lyrics = re.sub(r"^.*Lyrics","",lyrics)
    lyrics = re.sub(r"\\x..","",lyrics)
    lyrics = re.sub(r"\d*Embed","",lyrics)
    lyrics = re.sub(r"You might also like","",lyrics)
    return lyrics


