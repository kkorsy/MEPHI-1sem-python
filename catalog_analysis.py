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
    return f'"{movie["title"]}" ({movie["year"]}) — {movie["rating"]}/10, ' \
        f'{duration_in_hours(movie["duration_min"])}, ' \
        f'жанры: {', '.join(sorted(list(movie["genres"])))}'

if __name__ == "__main__":
    main()
