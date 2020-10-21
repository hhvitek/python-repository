#!/usr/bin/env python

"""
Using 3rd party library imap-tools 0.15.0
Seem pretty unstable to meeeeee
Fetch method workd pretty weirdly
"""

import logging
from imap_tools import MailBox
from settings import Settings

if __name__ == "__main__":
    logging.basicConfig(
        format="%(asctime)s|%(levelname)s|%(filename)s|%(funcName)s||%(message)s",
        level=logging.INFO,
        datefmt="%H:%M:%S",
    )

    logging.info("STARTING using MailBox")

    settings = Settings("./.settings.ini")
    USERNAME = settings.get_username()
    PASSWORD = settings.get_password()
    SERVER = settings.get_server()

    mailbox = MailBox(SERVER)
    mailbox.login(USERNAME, PASSWORD, initial_folder="INBOX")

    mailbox.seen(mailbox.fetch("(UNSEEN)"), False)

    mailbox.logout()
    logging.info("FINISHED")
