class MovieDetails:

    def __init__(self, name, artist, year, ratings):
        self.name = name
        self.artist = artist
        self.year = year
        self.ratings = ratings

    def display(self):
        print("The Movie: ", self.name)
        print("The Artist Name: ", self.artist)
        print("Release Year : ", self.year)
        print("Ratings: ", self.ratings)

    def update(self):
        name = input("Enter the name of the movie: ")
        self.name = name
        artist = input("Enter the name of the artist: ")
        self.artist = artist
        year = input("Enter the year of release: ")
        self.year = year
        ratings = float(input("Enter the ratings of movie released: "))
        self.ratings = ratings
        print("Movie: ", self.name)
        print("Artist Name: ", self.artist)
        print("Year of release: ", self.year)
        print("Ratings: ", self.ratings)

movie = MovieDetails("James Bond","Daniel Crag","2010", 7.8)
movie.display()
movie.update()