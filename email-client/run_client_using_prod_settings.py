#!/usr/bin/env python

import logging
import imaplib
from settings import Settings


def unseen_all_messages_in_folder(server, folder):

    server.select(folder)

    typ, data = server.search(None, "UNSEEN")
    for num in data[0].split():
        typ, data = server.fetch(num, "(RFC822)")


if __name__ == "__main__":
    logging.basicConfig(
        format="%(asctime)s|%(levelname)s|%(filename)s|%(funcName)s||%(message)s",
        level=logging.INFO,
        datefmt="%H:%M:%S",
    )

    logging.info("STARTING core python lib imaplib")

    settings = Settings("./.ignore_this_prod_settings.ini")
    USERNAME = settings.get_username()
    PASSWORD = settings.get_password()
    SERVER = settings.get_server()

    server = imaplib.IMAP4_SSL(SERVER)
    server.login(USERNAME, PASSWORD)

    unseen_all_messages_in_folder(server, "INBOX")
    unseen_all_messages_in_folder(server, "newsletters")
    unseen_all_messages_in_folder(server, "archive")

    server.close()
    server.logout()

    logging.info("FINISHED")
