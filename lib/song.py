class Song:
    pass
class Song:
    count = 0
    genres = []  # List of unique genres
    artists = []  # List of unique artists
    genre_count = {}  # Dictionary to count songs per genre
    artist_count = {}  # Dictionary to count songs per artist

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1  # Increments the total song count

    @classmethod
    def add_to_genres(cls, genre):
        """Adds a genre to the genres list if it's not already present."""
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        """Adds an artist to the artists list if it's not already present."""
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        """Tracks the count of songs per genre."""
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1  # Initialize genre count

    @classmethod
    def add_to_artist_count(cls, artist):
        """Tracks the count of songs per artist."""
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1  # Initialize artist count


# **Testing the Implementation**
song1 = Song("Song1", "Artist1", "Pop")
song2 = Song("Song2", "Artist2", "Rock")
song3 = Song("Song3", "Artist1", "Pop")  # Same artist, same genre
song4 = Song("Song4", "Artist3", "Rap")

print("Total songs:", Song.count)  # Expected: 4
print("Unique genres:", Song.genres)  # Expected: ['Pop', 'Rock', 'Rap']
print("Unique artists:", Song.artists)  # Expected: ['Artist1', 'Artist2', 'Artist3']
print("Genre count:", Song.genre_count)  # Expected: {'Pop': 2, 'Rock': 1, 'Rap': 1}
print("Artist count:", Song.artist_count)  # Expected: {'Artist1': 2, 'Artist2': 1, 'Artist3': 1}
