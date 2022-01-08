class SongRecord():
    
    def __init__(self, artist, track_title, album, year):
        self.artist = artist
        self.track_title = track_title
        self.album = album
        self.year = year
    
     def __str__(self):
        return (
            f"Performer: {self.artist}\n"
            f"Song: {self.track_title.rjust(5 + len(self.track_title))}\n"
            f"Album: {self.album.rjust(4 + len(self.album))}\n"
            f"Year: {str(self.year).rjust(5 + len(str(self.year)))}\n"
        )
song_record1 = SongRecord("Twenty One Pilots", "Fake you out", "Vessel", 2013)
song_record2 = SongRecord("Imagine Dragons", "Roots", "Evolve", 2015)
song_record3 = SongRecord("Queen", "Don't Stop Me Now", "Jazz", 1979)
print(song_record1)
print(song_record2)
print(song_record3)

