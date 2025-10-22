import time

epoch_date = time.strftime("%B %d, %Y", time.gmtime(0))
seconds = time.time()  # Return seconds since Epoch

print(
    f"Seconds since {epoch_date}: {seconds:,.4f} or {seconds:.2e} in "
    "scientific notation\n" + time.strftime("%b %d %Y")
)
