import random
def random_movie():  
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 23, 24, 25, 26, 27, 28]

    list_of_random_movies = [ 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
    for i in range(4): 
        random_item = random.choice(list_of_random_movies)
        list. append(random_item)
        list_of_random_movies. remove(random_item)
        return list
    
    print(random_movie()) 