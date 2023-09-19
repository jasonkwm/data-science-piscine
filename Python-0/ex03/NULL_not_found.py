

def NULL_not_found(object: any) -> int:
    isNan = float("nan")
    # print(object != object)
    if (object == None):
        print("Nothing: {} {}".format(object, type(object)))
    elif (type(isNan) == type(object) and object != object):
        print("Cheese: {} {}".format(object, type(object)))
    elif (object == 0 and type(object) == type(int())):
        print("Zero: {} {}".format(object, type(object)))
    elif (object == "" and type(object) == type(str())):
        print("Empty: {} {}".format(object, type(object)))
    elif (object == False):
        print("Fake: {} {}".format(object, type(object)))
    else:
        print("Type not Found")
        return 1
    return 42