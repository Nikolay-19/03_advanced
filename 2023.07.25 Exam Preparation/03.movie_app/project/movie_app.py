from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def existing_user(self, username):
        for el in self.users_collection:
            if el.username == username:
                return True
        return False

    def existing_movie(self, movie):
        for el in self.movies_collection:
            if el.title == movie.title:
                return True
        return False

    def get_user(self, username):
        for el in self.users_collection:
            if el.username == username:
                return el

    def register_user(self, username, age):
        user = User(username, age)
        if self.existing_user(username):
            raise Exception("User already exists!")
        self.users_collection.append(user)
        return f"{username} registered successfully."

    def upload_movie(self, username, movie):
        if not self.existing_user(username):
            return "This user does not exist!"
        user = self.get_user(username)
        if movie not in user.movies_owned:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        if self.existing_movie(movie):
            raise Exception("Movie already added to the collection!")

        user.movies_owned.append(movie)
        self.movies_collection.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username, movie, **kwargs):
        user = self.get_user(username)

        if not self.existing_movie(movie):
            raise Exception(f"The movie {movie.title} is not uploaded!")
        if movie not in user.movies_owned:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for key, value in kwargs.items():
            setattr(movie, key, value)
        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username, movie):
        user = self.get_user(username)

        if not self.existing_movie(movie):
            raise Exception(f"The movie {movie.title} is not uploaded!")
        if movie not in user.movies_owned:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        user.movies_owned.remove(movie)
        self.movies_collection.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username, movie):
        user = self.get_user(username)
        if movie in user.movies_owned:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")
        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        movie.likes += 1
        user.movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username, movie):
        user = self.get_user(username)
        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        user.movies_liked.remove(movie)
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if not self.movies_collection:
            return "No movies found."
        result = []
        sorted_movies = sorted(self.movies_collection, key=lambda x: (-x.year, x.title))
        for el in sorted_movies:
            result.append(el.details())
        return "\n".join(str(el) for el in result)

    def __str__(self):
        result = []
        if self.users_collection:
            result.append(f"All users: {', '.join(str(el.username) for el in self.users_collection)}")
        else:
            result.append("All users: No users.")
        if self.movies_collection:
            result.append(f"All movies: {', '.join(str(el.title) for el in self.movies_collection)}")
        else:
            result.append("All movies: No movies.")
        return "\n".join(str(el) for el in result)
