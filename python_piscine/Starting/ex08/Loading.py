from time import time
from time import perf_counter

def ft_tqdm(lst: range) -> None:
    range_end = lst[-1] + 1
    start_time = perf_counter() * 10**6 
    yield
    for n in lst:
        elapsed_time = start_time - perf_counter()
        frequency = (n / elapsed_time) * 10**6
        eta = (range_end - n - 1) / frequency if frequency else 0
        completion_proportion = ((n+1)*100) // range_end
        progress_bar = f"{str(completion_proportion)}%| [{'=' * completion_proportion}>{' ' * (100 - completion_proportion)}]| {str(n+1)} / {str(range_end)} [eta: {eta:.1f}s, {frequency:.2f}it/s]"
        print(progress_bar, end="\r")
        start_time = perf_counter() * 10**6 
        yield
