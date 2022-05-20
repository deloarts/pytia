def check_type(object_, type_):
    if not isinstance(object_, type_):
        raise TypeError(f"Wrong type. Expected type {type_}.")
    pass
