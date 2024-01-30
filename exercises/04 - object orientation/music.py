class Track():
    def __init__(self, description, length):
        self.description = description
        self.length = length

class CR_ROM():
    def __init__(self):
        pass

    def add_track(self, track):
        if self.can_add_track(track):
            self.tracks.append(track)
        else:
            print("Cannot add track")
    
    def total(self):
        return sum(map(lambda t: t.length, self.tracks))

    def can_add_track(self, track):
        return self.total + track.length <= 74