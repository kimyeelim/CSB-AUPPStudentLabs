class Song:
    def __init__(self, title, artist, album, genre, length):
        self.title = title
        self.artist = artist
        self.album = album
        self.genre = genre
        self.length = length

class MusicLibrary:
    def __init__(self):
        self.songs = {}

    def add_song(self, song):
        # Using a unique identifier as the key to prevent duplicates
        song_id = hash((song.title, song.artist, song.album, song.genre, song.length))
        self.songs[song_id] = song

    def get_songs_by_artist(self, artist):
        return [song for song in self.songs.values() if song.artist == artist]

    # Implement other retrieval methods (by album, genre, title)

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = set()

    def add_song(self, song):
        # Using a set to prevent duplicates in the playlist
        self.songs.add(song)

    def remove_song(self, song):
        self.songs.remove(song)

    def reorder_songs(self, new_order):
        # Implement reordering logic
        pass

    def display_playlist(self):
        print(f"Playlist: {self.name}")
        for index, song in enumerate(self.songs, start=1):
            print(f"{index}. {song.title} - {song.artist}")

# Sample usage
song1 = Song("Song 1", "Artist 1", "Album 1", "Genre 1", "3:30")
song2 = Song("Song 2", "Artist 2", "Album 2", "Genre 2", "4:15")

music_library = MusicLibrary()
music_library.add_song(song1)
music_library.add_song(song2)

playlist1 = Playlist("My Playlist 1")
playlist1.add_song(song1)
playlist1.add_song(song2)

playlist1.display_playlist()

songs_by_artist = music_library.get_songs_by_artist("Artist 1")
print(f"Songs by Artist 1: {', '.join([song.title for song in songs_by_artist])}")
