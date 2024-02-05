# 1 Task
def above(movie):
    return movie["imdb"] > 5.5

# 2 Task
def movies(movies_list):
    return [movie for movie in movies_list if above(movie)]

# 3 Task
def category(movies_list, category):
    return [movie for movie in movies_list if movie["category"] == category]

# 4 Task
def average_imdb_score(movies_list):
    if not movies_list:
        return 0.0
    total_score = sum(movie["imdb"] for movie in movies_list)
    return total_score / len(movies_list)

# 5 Task
def average_imdb_score_by_category(movies_list, category):
    category_movies = category(movies_list, category)
    return average_imdb_score(category_movies)