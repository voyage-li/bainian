import os
import time

print("\033[?25l")

for i in range(1, 1801):
    print("\033c")
    os.system("cat ./_txt/"+str(i)+".txt")
    time.sleep(0.04)
print("\033[?25h")
