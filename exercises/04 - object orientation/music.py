class Track():
    def __init__(self, description, length: int) -> None:
        self.description = description
        self.length = length
    
    def __str__(self) -> str:
        return self.description
    
    def __eq__(self, other) -> bool:
        return self.description == other.description

class CD_ROM():
    def __init__(self, max_length=74) -> None:
        self.tracks = []
        self.max_length = max_length
    
    def __str__(self) -> str:
        res = []
        res.append("-- CD_ROM --")
        res.append(f"Max_lenght: {self.max_length}")
        res.append(f"Length: {self.total()}")
        
        str_tracks = ", ".join(map(str, self.tracks))
        res.append(f"Tracks: [{str_tracks}]")
        
        return "\n".join(res)

    def add_track(self, track: Track) -> bool:
        if self.can_add_track(track):
            self.tracks.append(track)
            print(f"Track {track} added")
            return True
        else:
            print("Cannot add track", track)
            return False
    
    def total(self) -> int:
        return sum(map(lambda t: t.length, self.tracks))

    def can_add_track(self, track: Track) -> bool:
        return self.total() + track.length <= self.max_length

cd = CD_ROM()
t1 = Track("1",50)
t2 = Track("2",20)
t3 = Track("3",30)

print(cd)
cd.add_track(t1)
cd.add_track(t2)
cd.add_track(t3)
print(cd)