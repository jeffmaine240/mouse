#!/usr/bin/env python3

import pyautogui
import time
import random
import logging
from datetime import datetime, timedelta

logging.basicConfig(
    filename='/tmp/mouse_activity.log',
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logging.getLogger().addHandler(logging.StreamHandler())

def stay_active(interval_minutes: float, max_runtime_minutes: float):
    start_time = time.time()
    end_time = start_time + (max_runtime_minutes * 60)

    screen_width, screen_height = pyautogui.size()
    center_x = screen_width // 2
    center_y = screen_height // 2

    logging.info(f"Starting vertical scroll activity: interval={interval_minutes} min, duration={max_runtime_minutes} min")

    while time.time() < end_time:
        now = datetime.now()

        rand_x = random.randint(0, screen_width - 1)
        rand_y = random.randint(0, screen_height - 1)
        pyautogui.moveTo(rand_x, rand_y, duration=0.5)
        logging.info(f"Moved to random position: ({rand_x}, {rand_y})")

        pyautogui.moveTo(center_x, center_y, duration=0.5)
        logging.info(f"Moved to center: ({center_x}, {center_y})")

        scroll_amount = random.randint(100, 300)
        pyautogui.scroll(scroll_amount)
        time.sleep(3)
        pyautogui.scroll(-scroll_amount)
        logging.info(f"Scrolled up and down by {scroll_amount} units")

        
        next_run = now + timedelta(minutes=interval_minutes)
        logging.info(f"Next action scheduled for ~{next_run.strftime('%Y-%m-%d %H:%M:%S')}")

        time.sleep(interval_minutes * 60)

    logging.info("Activity session complete.")

if __name__ == "__main__":
    # Example: Run every 0.5 minute for 10 minutes
    stay_active(interval_minutes=0.5, max_runtime_minutes=10)
