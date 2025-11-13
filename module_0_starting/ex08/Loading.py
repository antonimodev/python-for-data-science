from time import perf_counter


def ft_tqdm(lst: range):
    total_it = len(lst)
    bar_length = 100

    start_time = perf_counter()
    for curr_it, elem in enumerate(lst):
        total_time = perf_counter() - start_time
        mins, secs = divmod(int(total_time), 60)
        curr_time = f"{mins:02d}:{secs:02d}"

        progress = ((curr_it + 1) / total_it)

        if (curr_it > 0):
            est_time = (total_time / (curr_it + 1)) * total_it
        else:
            est_time = 0
        est_mins, est_secs = divmod(int(est_time), 60)
        est_final_time = f"{est_mins:02d}:{est_secs:02d}"

        filled_length = int(bar_length * progress)
        bar = '█' * filled_length + ' ' * (bar_length - filled_length)

        if total_time > 0:
            it_per_sec = (curr_it + 1) / total_time
        else:
            it_per_sec = 0

        print(f"{progress * 100:3.0f}%", end='|')
        print(f"{bar}|", end=' ')
        print(f"{curr_it + 1}/{total_it}", end=' ')
        print(f"[{curr_time}<{est_final_time},", end=' ')
        print(f"{it_per_sec:.2f}it/s]", end='\r')
        yield elem
    print()
