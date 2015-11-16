__author__ = 'koo'

from msgManager import *
from udpSocket import *
import time

# Start from main menu.
# at 3 sec, user clicks Study button.

TIME_INTERVAL = 1.0

def send_msg(s, tick):
    if tick >= 3 and tick <= 5:
        msg = make_msg(STUDY_X, STUDY_Y, 0, 0)
    elif tick == 10:
        msg = make_msg(0, 0, CHECK1_X, CHECK1_Y)
    elif tick == 15:
        msg = make_msg(0, 0, CHECK2_X, CHECK2_Y)
    elif tick == 20:
        msg = make_msg(0, 0, CHECK3_X, CHECK3_Y)
    else:
        msg = make_random_msg()

    s.sendto(msg, SERVER_ADDR)


if __name__ == "__main__":
    s = init_socket()

    tick = 0
    start_time=time.time()

    while True:
        send_msg(s, tick)
        tick = tick + 1
        time.sleep(TIME_INTERVAL - ((time.time() - start_time) % TIME_INTERVAL))

