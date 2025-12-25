def main():
    # yell(["This", "is", "CS50"])
    yell("This", "is", "CS50")
    
def yell(*words):
    # method 1
    # uppercased = []
    # for word in words:
    #     uppercased.append(word.upper())
    # method 2
    # uppercased = map(str.upper, words)
    # method 3
    # list comprehension
    uppercased = [word.upper() for word in words]
    print(*uppercased)
    
    
if __name__ == "__main__":
    main()