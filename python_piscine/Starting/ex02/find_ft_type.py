def all_thing_is_obj(object: any) -> int:
    t = type(object)
    type_name = t.__name__
    print(object + " is in the kitchen :" , end=" ") if type_name == "str" else print(type_name, end=" : ")
    print(t)
    return 42