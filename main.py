# -*- coding: utf-8 -*-
from simple_bot import Bot
from longpoll_bot import LongPollBot

if __name__ == "__main__":
    longpoll_bot = LongPollBot()
    longpoll_bot.run_long_poll()
