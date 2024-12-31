chemi_ojaxi = {
    "brand":"deda",
    "year":"32",
}


print(chemi_ojaxi["brand"])
print(chemi_ojaxi.get("brand"))



chemi_ojaxi["color"] = "red"
chemi_ojaxi.setdefault("Tamuna_chvritidze", "Misho_oshoridze")
print(chemi_ojaxi)