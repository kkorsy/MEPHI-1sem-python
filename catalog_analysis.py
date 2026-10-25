import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, 
     "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]


def main():
    print_not_comedies(movies)
    print_high_rated_movies(movies)

def average_rating(movies):
    return round(sum(movie["rating"] for movie in movies) / len(movies), 1)

def catalog_age_stats(movies, current_year=2026):
    oldest_movie = max(current_year - movie["year"] for movie in movies)
    newest_movie = min(current_year - movie["year"] for movie in movies)
    avg_year = sum(current_year - movie["year"] for movie in movies) / len(movies)
    return (oldest_movie, newest_movie, math.ceil(avg_year))

def duration_in_hours(minutes):
    return f"{minutes // 60}ч {minutes % 60}м"

def rating_tier(rating):
    category = ""
    if rating >= 9:
        category = "шедевр"
    elif rating >= 7:
        category = "хорошо"
    else:
        category = "средне" if rating >= 5 else "слабо"
    return category

def decade_label(year):
    match year:
        case _ if year >= 2021:
            return "новые"
        case _ if 2020 >= year >= 2015:
            return "недавние"
        case _:
            return "старые"

def print_not_comedies(movies):
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue
        print(movie["title"])

def find_first_masterpiece(movies):
    i = 0
    while i < len(movies):
        if rating_tier(movies[i]["rating"]) == "шедевр":
            break
        i += 1
    else:
        print("Шедевров не найдено")
        return
    return movies[i]

def count_long_movies(movies, threshold=120):
    cnt = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            cnt += 1
    return cnt

def normalize_title(title):
    capitalized_title = ""
    words = title.split()
    for word in words:
        capitalized_title += word[0].upper() + word[1:] + " "
    return capitalized_title.strip()

def make_slug(title: str):
    return title.lower().replace(" ", "-")

def format_report_line(movie):
    return f'"{normalize_title(movie["title"])}" ({movie["year"]}) — ' \
        f'{movie["rating"]}/10, {duration_in_hours(movie["duration_min"])}, ' \
        f'жанры: {', '.join(sorted(list(movie["genres"])))}'

def titles_sorted_by_rating(movies: list):
    sorted_movies = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    return [movie["title"] for movie in sorted_movies]

def top_n_by_rating(movies, n=3):
    sorted_movies = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    return [(movie["title"], movie["rating"]) for movie in sorted_movies[:n]]

def count_by_genre(movies):
    genres_cnt = {}
    for movie in movies:
        for genre in movie["genres"]:
            genres_cnt[genre] = genres_cnt.get(genre, 0) + 1
    return genres_cnt

def actor_filmography(movies):
    actor_films = {}
    for movie in movies:
        for actor in movie["actors"]:
            actor_films[actor] = actor_films.get(actor, []) + [movie["title"]]
    return actor_films

def high_rating_movies(movies):
    return {movie["title"]: movie["rating"] for movie in movies \
            if movie["rating"] > average_rating(movies)}

def all_genres(movies):
    genres = set()
    for movie in movies:
        genres.update(movie["genres"])
    return genres

def common_actors(movie1, movie2):
    return set(movie1["actors"]) & set(movie2["actors"])

def genres_only_in_one(movies_a, movies_b):
    genres_a = set()
    for movie in movies_a:
        genres_a.update(movie["genres"])
    genres_b = set()
    for movie in movies_b:
        genres_b.update(movie["genres"])
    return genres_a - genres_b

def iter_high_rated(movies, min_rating=8.0):
    for movie in filter(lambda movie: movie["rating"] >= min_rating, movies):
        yield movie

def print_high_rated_movies(movies):
    for movie in iter_high_rated(movies):
        print(format_report_line(movie))

def sum_movies_duration(movies):
    return sum(movie["duration_min"] for movie in movies if movie["rating"] > 7)

if __name__ == "__main__":
    main()
