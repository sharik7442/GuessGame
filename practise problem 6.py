import random
def guessgame(a,b, actual):
    guess=int(input(f"guess a number between {a} and {b}\n"))
    nguess=11
    while guess!=actual:
        if guess<actual:
            guess=int(input(f"enter a bigger number\n"))
            nguess+=1

        else:
            guess=int(input(f"enter a smaller number\n"))
            nguess+=1

    print(f"you guessed the number in {nguess} guesses\n")
    return nguess


if __name__ == '__main__':
    a=int(input("enter the value of a\n"))
    b=int(input("enter the value of b\n"))
    actual1=random.randint(a,b)
    print("sharik's turn\n")
    g1=guessgame(a,b, actual1)
    print("sonam's turn\n")
    actual2 = random.randint(a, b)
    g2=guessgame(a,b, actual2)

    if g1 < g2:
        print("sharik won the match\n")

    elif g1 > g2:
        print("sonam  won the match\n")

    else:
        print("its a tie\n")


    print(f"the correct number for sharik was {actual1} and for sonam was {actual2}")
