class Album:
    # Constructor
    def __init__(self, title, artist, price, genre):
        self.title = title
        self.artist = artist
        self.price = price
        self.genre = genre

    # Getters
    def getTitle(self):
        return self.title

    def getArtist(self):
        return self.artist

    def getPrice(self):
        return self.price

    def getGenre(self):
        return self.genre

    # Setters
    def setTitle(self, title):
        self.title = title

    def setArtist(self, artist):
        self.artist = artist

    def setPrice(self, price):
        self.price = price

    def setGenre(self, genre):
        self.genre = genre


class Review:
    # Constructor
    def __init__(self, title, description, score):
        self.title = title
        self.review = description
        self.score = score

    # Getters
    def getTitle(self):
        return self.title

    def getReview(self):
        return self.review

    def getScore(self):
        return self.score

    # Setters
    def setTitle(self, title):
        self.title = title

    def setReview(self, review):
        self.review = review

    def setScore(self, score):
        self.score = score
