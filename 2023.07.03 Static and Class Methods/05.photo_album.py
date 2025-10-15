from math import ceil


class PhotoAlbum:
    LIMIT = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = []
        for _ in range(pages):
            self.photos.append([])

    @classmethod
    def from_photos_count(cls, photos_count):
        pages = ceil(photos_count / PhotoAlbum.LIMIT)
        return cls(pages)

    def add_photo(self, label):
        for row in range(len(self.photos)):
            if len(self.photos[row]) == PhotoAlbum.LIMIT:
                continue
            self.photos[row].append(label)
            return f"{label} photo added successfully on page {row + 1} slot {len(self.photos[row])}"
        else:
            return "No more free slots"

    def display(self):
        result = ["-----------"]
        for row in range(len(self.photos)):
            result.append("".join("[] " * len(self.photos[row])))
            result.append("-----------")
        for el in range(len(result)):
            if el % 2 != 0:
                result[el] = result[el][:-1]

        return "\n".join(str(el) for el in result)
