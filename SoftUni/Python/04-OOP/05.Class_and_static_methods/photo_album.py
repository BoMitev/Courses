import math


class PhotoAlbum:
    MAX_PICTURES_PER_PAGE = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        pages = math.ceil(photos_count / PhotoAlbum.MAX_PICTURES_PER_PAGE)
        return cls(pages)

    def add_photo(self, label: str):
        for page in range(len(self.photos)):
            if PhotoAlbum.MAX_PICTURES_PER_PAGE > len(self.photos[page]):
                self.photos[page].append(label)
                return f"{label} photo added successfully on page {page+1} slot {len(self.photos[page])}"
        return f"No more free slots"

    def display(self):
        info = []
        for page in self.photos:
            page = ['[]' for _ in range(len(page))]
            info.append('-' * 11)
            info.append(' '.join(page))

        info.append('-' * 11)
        return '\n'.join(info)

album = PhotoAlbum(2)
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
