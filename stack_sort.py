def sort(width, height, length, mass):
    volume = width * height * length

    bulky = volume >= 1000000 or width >= 150 or height >= 150 or length >= 150
    heavy = mass >= 20

    if bulky and heavy:
        print("REJECTED")
    elif bulky or heavy:
        print("SPECIAL")
    else:
        print("STANDARD")
