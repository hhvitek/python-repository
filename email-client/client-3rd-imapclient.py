#!/usr/bin/env python

"""
Using 3rd party library IMAPClient 2.1.0
"""

import logging
from imapclient import IMAPClient
from settings import Settings

if __name__ == "__main__":
    logging.basicConfig(
        format="%(asctime)s|%(levelname)s|%(filename)s|%(funcName)s||%(message)s",
        level=logging.INFO,
        datefmt="%H:%M:%S",
    )

    logging.info("STARTING using IMAPClient")

    settings = Settings("./.settings.ini")
    USERNAME = settings.get_username()
    PASSWORD = settings.get_password()
    SERVER = settings.get_server()

    server = IMAPClient(SERVER)
    server.login(USERNAME, PASSWORD)

    select_info = server.select_folder("INBOX")
    print(select_info)

    messages = server.search("UNSEEN")
    server.fetch(messages, "RFC822")

    server.logout()

    logging.info("FINISHED")
