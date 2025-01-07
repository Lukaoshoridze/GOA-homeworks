nayini = {

    1 : "shokoladis nayini",
    False : "cocosis nayini",
    "name_2" : "kargi nayini",
}

print("---------------------.get-----------------------------")
print(nayini.get(1))
print(nayini.get(False))
print(nayini.get("name_2"))
print("---------------------.get-----------------------------")



print("-----------------.in----------------------------------------------------------------------------")
if "name_2" in nayini:
    print(F" kargi nayin chans"{nayini['name_2']})
          
if "kargi nayini" not in nayini:
    print("kaia! mec maseti nayini miyvars")

print("----------------.in------------------------------------------------------------------------------")