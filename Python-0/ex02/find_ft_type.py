def NULL_not_found(object: any) -> int:
    if (type(object) == type("")):
        print("{} is in the kitchen : {}".format(object, type(object)))
    elif (type(object) == type(dict())):
        print("Dict : {}".format(type(object)))
    elif (type(object) == type(list())):
        print("List : {}".format(type(object)))
    elif (type(object) == type(tuple())):
        print("Tuple : {}".format(type(object)))
    elif (type(object) == type(set())):
        print("Set : {}".format(type(object)))
    else:
        print("Type not found")
    return 42

