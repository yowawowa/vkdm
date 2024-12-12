# -*- coding: utf-8 -*-
from longpoll_bot import LongPollBot
import requests
from dotenv import load_dotenv
import os

load_dotenv()

if __name__ == "__main__":
    try:
        longpoll_bot = LongPollBot()
        longpoll_bot.run_long_poll()
    except Exception as e:
        requests.post(
            f"https://ntfy.sh/{os.getenv("NTFY_TOPIC")}",
            data="vkdm crashed".encode(encoding="utf-8"),
        )
