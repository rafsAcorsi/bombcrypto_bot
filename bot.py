#!/bin/env python3
# on 08 Jan 2022
import datetime
import os
import time

import pyautogui

pyautogui.FAILSAFE = False

GAME_URL = "https://app.bombcrypto.io/webgl/index.html"

CONFIG = {
    # minutes
    "sleep_time": 60,
    "refresh_map_time": 20,
    # minutes
    "refresh_map": 2,
    "profiles": [
        {
            "name": "User1",
            "refresh": (96, 90, 'left'),
            "login_metamask": (401, 626, 'left'),
            "login_game": (256, 355, 'left'),
            "btn_heroes": (456, 388, 'left'),
            "btn_close_heroes": (284, 174, 'left'),
            "btn_work_all": (210, 197, 'left'),
            'btn_initial_window': (36, 133, 'left'),
            'btn_enter_game': (256, 270, 'left')
        },
        {
            "name": "User2",
            "refresh": (597, 91, 'left'),
            "login_metamask": (897, 629, 'left'),
            "login_game": (750, 354, 'left'),
            "btn_heroes": (956, 387, 'left'),
            "btn_close_heroes": (781, 173, 'left'),
            "btn_work_all": (711, 199, 'left'),
            'btn_initial_window': (534, 135, 'left'),
            'btn_enter_game': (752, 262, 'left')
        },
        {
            "name": "User3",
            "refresh": (1100, 93, 'left'),
            "login_metamask": (1408, 629, 'left'),
            "login_game": (1250, 354, 'left'),
            "btn_heroes": (1457, 387, 'left'),
            "btn_close_heroes": (1284, 173, 'left'),
            "btn_work_all": (1209, 199, 'left'),
            'btn_initial_window': (1037, 135, 'left'),
            'btn_enter_game': (1250, 262, 'left')
        },
    ]
}


def print_time(text=None, minutes=None):
    now = datetime.datetime.now()
    if minutes:
        now = now + datetime.timedelta(minutes=minutes)
    print(f"{text} {now.strftime('%H:%M:%S')}")


def push_button(message: str = None, coord: tuple = None, sleep: int = None):
    print_time(text=f"{message}")

    # try 2 times
    pyautogui.mouseDown(*coord)
    pyautogui.mouseUp(*coord)
    time.sleep(1)
    pyautogui.mouseDown(*coord)
    pyautogui.mouseUp(*coord)

    if sleep:
        time.sleep(sleep)


def run():
    while True:
        start_date = datetime.datetime.now()
        for profile in CONFIG['profiles']:
            print_time(text=f"Start JOB {profile['name']}")

            push_button(
                message=f"Refresh PAGE {profile['name']}",
                coord=profile["refresh"],
                sleep=12
            )

            push_button(
                message="Login",
                coord=profile["login_game"],
                sleep=12
            )

            push_button(
                message="Login Metamask",
                coord=profile["login_metamask"],
                sleep=30
            )

            push_button(
                message="Hero select",
                coord=profile["btn_heroes"],
                sleep=4
            )

            push_button(
                message="Go to Work",
                coord=profile["btn_work_all"],
                sleep=3
            )

            push_button(
                message="Close Hero Select",
                coord=profile["btn_close_heroes"],
                sleep=3
            )

            push_button(
                message="Enter the game",
                coord=profile["btn_enter_game"],
                sleep=5
            )

        while True:
            print_time("Next Interaction on", minutes=CONFIG['refresh_map'])
            time.sleep(CONFIG['refresh_map'] * 60)
            for profile in CONFIG['profiles']:
                push_button(
                    message=f"Refresh Position {profile['name']}",
                    coord=profile["btn_initial_window"],
                    sleep=5
                )

                push_button(
                    message="Back to the game",
                    coord=profile["btn_enter_game"],
                    sleep=1
                )

            sleep_time = CONFIG['sleep_time']
            refresh_map_time = CONFIG['refresh_map_time']
            now = datetime.datetime.now()
            if now >= (
                    start_date + datetime.timedelta(minutes=refresh_map_time)):
                print_time("Sleep until", minutes=sleep_time)
                time.sleep(sleep_time * 60)
                break


if __name__ == '__main__':
    run()
