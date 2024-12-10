import random
def random_movie():   #შევქმენით ფუნქცია
    list = ["interstellar", "inseption", "შერეკილები"]
    list_of_random_movies = ["მე ბებია ილიკო და ილარიონი", "ცისფერი მთები", "მამლუქი", "ბაშიაჩუქი",
    "წუნა და წრუწუნა", "ჩხიკვთა ქორწილი"]#აქ შეგვიძლია ჩავწეროთ პილმ ან მულთფილმი რომლებიც გვინდა
    for i in range(4): # 4 რომ ჩავწერეთ list_of_random_movies-ში 
        #რა ფილმი ან მულთფილმი არის მაქედან 4-ს გამოგვიტანს, მაგრამ 4-ის მაგივრად სხვა რიცხვის ჩაწერა შეგვიძლია
        random_item = random.choice(list_of_random_movies)
        list. append(random_item)
        list_of_random_movies. remove(random_item)
        return list
    
    print(random_movie()) #ეს ეხმარება რომ გამოგვიტანოს 4 პილმი ან 4 მულთფიმი, მ