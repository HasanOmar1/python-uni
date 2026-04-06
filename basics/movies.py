#1
def create_movies(list:list[dict]):
    for movie in list:
        print(movie)

#2
def print_movies(movies):
    for movie in movies:
        print(f"Title : {movie['title']}\nGenre : {movie['genre']}\nYear : {movie['year']}\nRating : {movie['rating']}")
        print("-----------------------------------")

#3
def average_rating(movies):
    if len(movies) == 0:
        return 0

    total = 0
    for movie in movies:
        if isinstance(movie['rating'], int):
            total += movie['rating']

    return total/len(movies)

#4
def high_rated_movies(movies):
    for movie in movies:
        if isinstance(movie['rating'], int):
            if movie['rating'] >= 8:
                print(movie)

#5
def get_movie_by_genre(movies , genre):
    for movie in movies:
        if movie['genre'].lower() == genre.lower():
            print(movie)

#6
def get_movie_by_title(movies, title):
    for movie in movies:
        if movie['title'].lower() == title.lower():
            print(movie)

#7
def is_movie_found(movies, title):
    is_found = False
    for movie in movies:
        if movie['title'].lower() == title.lower():
            is_found = True

    if not is_found:
        print("Movie not found")



def main():
    movies =[
      {
        "title": "Interstellar",
        "genre": "Sci-Fi",
        "year": 2014,
        "rating": 1
      },
      {
        "title": "The Lion King",
        "genre": "Kids",
        "year": 1994,
        "rating": 4
      },
      {
        "title": "Inception",
        "genre": "Action",
        "year": 2010,
        "rating": 3
      },
      {
        "title": "Spider-Man: Into the Spider-Verse",
        "genre": "Kids",
        "year": 2018,
        "rating": "asd"
      },
      {
        "title": "Mad Max: Fury Road",
        "genre": "Action",
        "year": 2015,
        "rating": 4
      },
      {
        "title": "Toy Story 4",
        "genre": "Kids",
        "year": 2019,
        "rating": 1
      },
      {
        "title": "The Dark Knight",
        "genre": "Action",
        "year": 2008,
        "rating": 10
      },
      {
        "title": "Dune: Part Two",
        "genre": "Sci-Fi",
        "year": 2024,
        "rating": 2
      },
      {
        "title": "Coco",
        "genre": "Kids",
        "year": 2017,
        "rating": 5
      },
      {
        "title": "John Wick",
        "genre": "Action",
        "year": 2014,
        "rating": 10
      }
    ]

    print("------------------- #8,9,10 -----------------")
    try:
        for movie in movies:
            if not isinstance(movie['rating'], int):
                raise TypeError("Type Error in rating in one of the movies")
            if not isinstance(movie['year'], int):
                raise TypeError("Type Error in year in one of the movies")
    except TypeError:
        print("Type Error in rating or year in one of the movies")
        with open("program_log.txt", "a", encoding="utf-8") as file:
            file.write("Type Error in rating or year in one of the movies\n")
    except Exception as e:
        print(e)
        with open("program_log.txt", "a", encoding="utf-8") as file:
            file.write(e, "\n")

    print("------------------- #1 -----------------")
    create_movies(movies)
    print("------------------- #2 -----------------")
    print_movies(movies)
    print("------------------- #3 -----------------")
    print("Average rating : ", average_rating(movies))
    print("------------------- #4 -----------------")
    print("Movies with 8+ rating")
    high_rated_movies(movies)
    print("------------------- #5 -----------------")
    genre = input("Enter genre: ")
    get_movie_by_genre(movies, genre)
    print("------------------- #6 -----------------")
    title = input("Enter title: ")
    get_movie_by_title(movies, title)
    print("------------------- #7 -----------------")
    is_movie_found(movies,title)


if __name__ == '__main__':
    main()