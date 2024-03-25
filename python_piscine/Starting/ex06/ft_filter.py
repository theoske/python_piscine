def ft_filter(function: any, iterable) -> object:
    filtered_iterable = type(iterable)()
    [filtered_iterable.append(item) for item in iterable if function(item)]
    return filtered_iterable
