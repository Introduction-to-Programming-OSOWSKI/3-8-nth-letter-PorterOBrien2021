def nthLetter(w, x):
    if x <= len(w):
        return w[x-1]

    else:
        return False

print(nthLetter("dog", 3))
