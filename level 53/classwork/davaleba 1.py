spiderman = {
    "brand":"qseli",
    "year":"2020",
}


print(spiderman["brand"])
print(spiderman.get("brand"))



spiderman["color"] = "black"
spiderman.setdefault("black spiderman", "red spidarman")
print(spiderman)