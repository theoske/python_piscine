def ft_tqdm(lst: range) -> None:
    i=0
    while i <= lst[-1]:
        last_in_range = lst[-1]
        completion_proportion = (i*100) // last_in_range
        print(str(completion_proportion) + "\%| [" + "=" * str(completion_proportion) + ">" + (" " * (100 - completion_proportion)) + "]| " + str(i) + str(lst))
        i+=1

