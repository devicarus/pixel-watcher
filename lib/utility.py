def inputBool(question):
    res = input(question + " (Y/n): ")
    if res.upper() == "Y":
        return True
    elif res == "":
        return True
    elif res.upper() == "N":
        return False
    else:
        return False