import time
from datetime import datetime 
import os
import pyfiglet

true = 1

while true:
     time.sleep(1)
     now = datetime.now()
     current_time = now.strftime("%H:%M:%S")
     os.system('cls' if os.name == 'nt' else 'clear')
     f = pyfiglet.figlet_format(current_time, justify="center", width=90, font="slant")
     print(f)