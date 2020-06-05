#!/usr/bin/env python

"""
Using 3rd party library imap-tools 0.15.0
Seem pretty unstable to meeeeee
Fetch method workd pretty weirdly
"""

import logging
from imap_tools import MailBox

if __name__ == "__main__":
    logging.basicConfig(
        format="%(asctime)s|%(levelname)s|%(filename)s|%(funcName)s||%(message)s",
        level=logging.INFO,
        datefmt="%H:%M:%S",
    )

    logging.info("STARTING")

    mailbox = MailBox("imap.seznam.cz")
    mailbox.login(USERNAME, PASSWORD, initial_folder="INBOX")

    # mailbox.seen(mailbox.fetch("(UNSEEN)"), False)
    # for message in mailbox.fetch('(UNSEEN)', charset='utf-8', mark_seen=False):
    #    print(message.headers())

    mailbox.logout()
    logging.info("FINISHED")
