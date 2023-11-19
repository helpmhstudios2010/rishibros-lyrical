class SpotifyLink:
    def __init__(self) -> None:
        
        import spotipy
        from spotipy.oauth2 import SpotifyOAuth

        # Set up your credentials
        SPOTIPY_CLIENT_ID = '5b2e343e38cc4d6398b830cef0210fb2'
        SPOTIPY_CLIENT_SECRET = '4c7068068ee94a89a6d148f98b37f195'
        SPOTIPY_REDIRECT_URI = 'http://localhost:8888/callback'  # This should be set in your Spotify Developer Dashboard

        # Set up the Spotify API authentication
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                                    client_secret=SPOTIPY_CLIENT_SECRET,
                                                    redirect_uri=SPOTIPY_REDIRECT_URI,
                                                    scope='user-read-playback-state'))

        # Get the current user's playback
        self.current_playback = sp.current_playback()

    # Extract information about the currently playing song
    def name(self):
        if self.current_playback != None and 'item' in self.current_playback:
            current_song_name = self.current_playback['item']['name']
            artists = self.current_playback['item']['artists']
            artists_names =[]
            for artist in artists:
                artists_names.append(artist['name'])            
            return current_song_name,artists_names
        else:
            return None,None
    def _duration(self):
        if self.current_playback is not None and 'item' in self.current_playback:
            return self.current_playback['item']['duration_ms']
    def _progress(self):
        if self.current_playback is not None and 'progress_ms' in self.current_playback:
            return self.current_playback['progress_ms']
        else:
            return None
    def time_remaining(self):
        if self.current_playback is not None and 'item' in self.current_playback:
            progress = self._progress()
            if progress!=None:
                duration = self._duration()
                return duration-progress
            else :
                return None



if __name__ == "__main__":
    pass