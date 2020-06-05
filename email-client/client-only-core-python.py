#!/usr/bin/env python

"""
Only Python core libraries
"""

import logging
import imaplib
from settings import Settings

if __name__ == "__main__":
    logging.basicConfig(
        format="%(asctime)s|%(levelname)s|%(filename)s|%(funcName)s||%(message)s",
        level=logging.INFO,
        datefmt="%H:%M:%S",
    )

    logging.info("STARTING")

    settings = Settings("./.settings.ini")
    USERNAME = settings.get_username()
    PASSWORD = settings.get_password()
    SERVER = settings.get_server()

    server = imaplib.IMAP4_SSL(SERVER)
    server.login(USERNAME, PASSWORD)
    server.select("INBOX")

    typ, data = server.search(None, "UNSEEN")
    for num in data[0].split():
        typ, data = server.fetch(num, "(RFC822)")

    server.close()
    server.logout()

    logging.info("FINISHED")
