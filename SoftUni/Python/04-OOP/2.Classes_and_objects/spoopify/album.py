class Album:
    def __init__(self, name, *songs):
        self.name = name
        self.published = False
        self.songs = list(songs)

    def add_song(self, song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"

        elif self.published:
            return f"Cannot add songs. Album is published."

        elif song in self.songs:
            return "Song is already in the album."

        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if self.published:
            return f"Cannot remove songs. Album is published."

        for song in self.songs:
            if song.name == song_name:
                self.songs.remove(song)
                return f"Removed song {song_name} from album {self.name}."

        return "Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."

        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        info = [f'Album {self.name}']
        info.extend([f'== {s.get_info()}' for s in self.songs])
        return '\n'.join(info)
