class Song:
    def __init__(self, artist, name, year):
        self.artist = artist
        self.name = name
        self.year = year

    def __repr__(self):
        rep = "Artist: {}. Name: {}. Year: {}".format(self.artist, self.name,
                                                      self.year)
        return rep

    def __str__(self):
        return "{} — {} ({})".format(self.artist, self.name, self.year)

if __name__ == '__main__':
      dsmn = Song("Queen", "Don't stop me now", 1979)
      print(dsmn)
