from db.database import Database

def obtener_movies(movie_id: int):
    # Obtén la colección "movies" desde la base de datos
    collection = Database.get_collection("movies")    
    # Obtén todas las películas de la base de datos, excluyendo el campo "_id"
    movies = collection.find_one({"id": movie_id}, {"_id": 0})   
    # Devuelve las películas obtenidas
    return movies
    .