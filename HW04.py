s = {"smart watch": 600, "phone": 1000, "playstation": 450, "laptop": 1550, "music player": 400, "tablet": 400}
amount = 1300

v1 = (s["smart watch"] + s["playstation"] + int(s["music player"] * 0.7))
v2 = (s["smart watch"] + s["music player"] + int(s["playstation"] * 0.7))
v3 = (s["playstation"] + s["music player"] + int(s["smart watch"] * 0.7))

print(v1, v2, v3)

if v1 <= amount:
    print("Yes! v1")
elif v2 <= amount:
    print("Yes! v2")
else:
    v3 <= amount
    print("Yes! v3")
