import time


def progressbar(lst):
    start = time.perf_counter()
    for i, n in enumerate(lst, 1):
        elapsed = time.perf_counter() - start
        percentage = int(i * 100 / len(lst))
        progress = f'{"=" * int(percentage / 5)}>'
        eta = elapsed * (100 - percentage) / (percentage if percentage else 1)
        print(f'ETA: {eta:.2f}s [{percentage:3}%][{progress:20}] {i}/{len(lst)} elapsed time {elapsed:.2f}s ', end='\r')
        yield n
