from sys import argv
if len(argv) == 2:
    try:
        number = int(argv[1])
        print("I'm Odd.") if number%2!=0 else print ("I'm Even.")
    except:
        print("AssertionError: argument is not an integer")
elif len(argv) > 2:
    print("AssertionError: more than one argument is provided")
else:
    print()