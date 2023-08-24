while True:
    print("Привет!")
    print("Hello!")
    print("Let's practice with `print()` and `input()` functions!")
    res = input("Are you in? (y/n) ")
    if res == "y":
        print("Yes! I knew it!")
        print("So, to print something, use `print()` function.")
        print("To input something, use `input()` function.")
        input("Press Enter to continue...")
        res = input("Do you want to continue? (y/n) ")
        if res == "y":
            print("Cool! But that is it! See you!")
        else:
            print("Fine! Anyway that's it! See you!")
        break
    else:
        print("Rude! Bye!")
        break
