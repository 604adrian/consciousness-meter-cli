import time
import sys

for i in range(4):
    sys.stdout.write('\rLoading...   ({0}%)'.format(i * 25))
    sys.stdout.flush()
    time.sleep(1)

sys.stdout.write('\rLoading...   (100%)\n')
sys.stdout.flush()

# Print green checkmark
print("\033[32m\u2714\033[0m")

