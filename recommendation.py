
# CODSOFT AI INTERNSHIP - TASK 4
# Movie Recommendation System

# Movie dataset
movies = {
    "Avatar": ["Sci-Fi", "Action", "Adventure"],
    "Interstellar": ["Sci-Fi", "Adventure", "Drama"],
    "Inception": ["Sci-Fi", "Action", "Thriller"],
    "Avengers": ["Action", "Adventure", "Sci-Fi"],
    "Titanic": ["Romance", "Drama"],
    "The Notebook": ["Romance", "Drama"],
    "John Wick": ["Action", "Thriller"],
    "The Dark Knight": ["Action", "Crime", "Drama"],
    "Frozen": ["Animation", "Adventure", "Family"],
    "Toy Story": ["Animation", "Adventure", "Comedy"],
    "Jumanji": ["Adventure", "Comedy", "Fantasy"],
    "The Conjuring": ["Horror", "Mystery", "Thriller"]
}

def recommend_movies(movie_name):
    selected = None

    for movie in movies:
        if movie.lower() == movie_name.lower():
            selected = movie
            break

    if selected is None:
        print("Movie not found in database!")
        return

    scores = []

    for movie, genres in movies.items():
        if movie != selected:
            score = len(
                set(movies[selected]) & set(genres)
            )
            if score > 0:
                scores.append((movie, score))

    scores.sort(key=lambda x: x[1], reverse=True)

    print("\nRecommended Movies:")
    if not scores:
        print("No similar movies found.")

    for i, (movie, score) in enumerate(scores[:5], 1):
        print(f"{i}. {movie}")

print("===== MOVIE RECOMMENDATION SYSTEM =====")
print("\nAvailable Movies:")

for movie in movies:
    print("-", movie)

while True:
    choice = input(
        "\nEnter your favourite movie (or 'exit'): "
    ).strip()

    if choice.lower() == "exit":
        print("Thank you for using Movie Recommender!")
        break

    recommend_movies(choice)
