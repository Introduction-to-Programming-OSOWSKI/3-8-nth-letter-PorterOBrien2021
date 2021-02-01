def nthLetter(w, x):
    if x <= len(w):
        return w[x]

    else:
        return False

print(nthLetter("dog", 3))
