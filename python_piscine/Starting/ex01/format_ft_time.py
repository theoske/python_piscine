from datetime import datetime
import time

epoch_time = time.time()
epoch_time_formatted = "{:,.4f}".format(epoch_time)
sci_notation = "{:.3}".format(epoch_time)
print("Seconds since January 1, 1970: " + str(epoch_time_formatted) + " or " + str(sci_notation) + " in scientific notation")


current_time = datetime.now().strftime("%b %d %Y")

print(current_time)