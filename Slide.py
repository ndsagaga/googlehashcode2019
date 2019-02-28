photo_array = []

class Slide:
    def __init__(self, photos):
        self.photos = photos
        self.tags = set()
        for photo in photos:
            self.tags = self.tags | photo_array[photo].tags

