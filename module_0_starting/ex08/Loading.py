import shutil
import sys
from collections.abc import Iterator
from time import perf_counter


def _test(nolint: list) -> None:
    name = "antonio"
    print(name)


def _format_time(seconds: float) -> str:
    """
    Format seconds into MM:SS string.

    Args:
        seconds: Time in seconds to format.

    Returns:
        Formatted time string in MM:SS format.
    """
    mins, secs = divmod(int(seconds), 60)
    return f"{mins:02d}:{secs:02d}"


def _build_progress_bar(current: int, total: int, elapsed: float, term_width: int) -> str:
    """
    Build the progress bar string for display, adapting to terminal width.

    Args:
        current: Current iteration (1-indexed).
        total: Total number of iterations.
        elapsed: Elapsed time in seconds.
        term_width: Width of the terminal in characters.

    Returns:
        Formatted progress bar string.
    """
    progress = current / total
    # Fixed text outside the bar
    prefix = f"{progress * 100:3.0f}%|"
    suffix = (
        f"| {current}/{total} "
        f"[{_format_time(elapsed)}"
        f"<{_format_time((elapsed / current) * total if current > 0 else 0.0)}, "
        f"{(current / elapsed) if elapsed > 0 else 0.0:.2f}it/s]"
    )
    # Calculate dynamic bar length
    bar_length = max(10, term_width - len(prefix) - len(suffix) - 1)
    filled = int(bar_length * progress)
    bar = "█" * filled + " " * (bar_length - filled)
    return f"{prefix}{bar}{suffix}"


def ft_tqdm(lst: range) -> Iterator[int]:
    """
    Display a progress bar for iterating over a range.

    Mimics the behavior of tqdm library, showing progress percentage,
    visual bar, iteration count, elapsed/estimated time, and speed.

    Args:
        lst: A range object to iterate over.

    Yields:
        Each element from the input range.
    """
    total = len(lst)
    is_tty = sys.stdout.isatty()
    term_width = shutil.get_terminal_size(fallback=(80, 20)).columns if is_tty else 80

    start_time = perf_counter()
    for idx, elem in enumerate(lst, start=1):
        elapsed = perf_counter() - start_time
        bar_str = _build_progress_bar(idx, total, elapsed, term_width)
        if is_tty:
            sys.stdout.write(f"\r{bar_str.ljust(term_width)}")
            sys.stdout.flush()
        yield elem

    if is_tty:
        sys.stdout.write("\n")
        sys.stdout.flush()
    else:
        print(_build_progress_bar(total, total, perf_counter() - start_time, term_width))
