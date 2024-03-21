def NULL_not_found(object:any) -> int:
    match type(object).__name__, object:
        case "NoneType", None:
            print("Nothing", end=": ")
            object_type = type(object)
            print(object, end=" ")
            print(object_type)
            return 0
        case "float", float(NaN):
            print("Cheese", end=": ")
            object_type = type(object)
            print(object, end=" ")
            print(object_type)
            return 0
        case "int", 0:
            print("Zero", end=": ")
            object_type = type(object)
            print(object, end=" ")
            print(object_type)
            return 0
        case "str", '':
            print("Empty", end=": ")
            object_type = type(object)
            print(object, end=" ")
            print(object_type)
            return 0
        case "bool", False:
            print("Fake", end=": ")
            object_type = type(object)
            print(object, end=" ")
            print(object_type)
            return 0
        case other:
            print("Type not Found")
            return 1