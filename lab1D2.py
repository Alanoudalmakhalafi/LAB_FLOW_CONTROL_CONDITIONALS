movie = "The Great Gatsby"
rating = 3
popularity = 72.65

if rating >= 4 and popularity > 80:
    print("highly recommended")

elif rating >= 3 and popularity > 70:
    print("I recommend it. It's good")

elif rating <= 2 and popularity > 60:
    print("you should check it out ")

else: print("Don't watch it. It is a waste of time")
