#3)
# შექმენით ფუნქცია
# სადაც იქნება ცარიელი სტრინგი
# და for loop ის გამოყენებით
# თქვენი სახლი რენდომულად დაამატეთ
# ამ ცარიელ სტრინგს <3

import random
def random_name():
    empty_string = ""
    my_name = " L u k a"  # აქ შეგიძლია ჩაწერო ის სიტყვა რაც გინდა 
    my_name_split = my_name. split() # split სიტყვას ასო ასო შლის, ხან რა ციპრებს გამოიტანს ხან რას
    for char in my_name_split:
        random_char = random. choice(my_name_split)
        empty_string += random_char
        my_name_split. remove(random_char) # ეს შლის random_char და გადადის " L u k a"-ზე
        return empty_string  #ეს აბრუნებს empty_string
    
    print(random_name())