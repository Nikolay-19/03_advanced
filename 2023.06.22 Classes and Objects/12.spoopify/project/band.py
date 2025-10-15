class Band:
    def __init__(self, name, albums=[]):
        self.name = name
        self.albums = albums

    def add_album(self, album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        for album in self.albums:
            if album.published:
                return "Album has been published. It cannot be removed."
            if album.name == album_name:
                self.albums.remove(album)
                return f"Album {album.name} has been removed."
        else:
            return f"Album {album_name} is not found."

    def details(self):
        result = [f"Band {self.name}"]
        for album in self.albums:
            result.append(album.details())
        return "\n".join(str(el) for el in result)
