import random
def random_movie():  
    list = ["lomi"]

    list_of_random_movies = ["vefxvi"]
    for i in range(4): 
        random_item = random.choice(list_of_random_movies)
        list. append(random_item)
        list_of_random_movies. remove(random_item)
        return list
    
    print(random_movie()) 