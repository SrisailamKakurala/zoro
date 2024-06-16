# checks the internet connectivity of user

import os

# check if user is offline or online 
def check_internet():
    response = os.system("ping -c 1 google.com" if os.name != "nt" else "ping -n 1 google.com")
    return response == 0

