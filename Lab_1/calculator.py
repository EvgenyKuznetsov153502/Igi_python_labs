def calculate(a, b, operation):
    match operation:
        case 'add':
            return a+b
        case 'sub':
            return a-b
        case 'mult':
            return a*b
        case 'div':
            if b == 0:
                print("can't divide by zero")
                return "could not be found"
            else:
                return a/b
        case _:
            print("incorrect input")
            return "could not be found"

