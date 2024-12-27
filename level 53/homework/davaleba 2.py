mancana = {
    "brand":"bevne",
    "year":"new",
}


print(mancana["brand"])
print(mancana.get("brand"))



mancana["color"] = "black"
mancana.setdefault("bevne", "porshe")
print(mancana)