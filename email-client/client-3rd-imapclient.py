#!/usr/bin/env python

"""
Using 3rd party library IMAPClient 2.1.0
"""

import logging
from imapclient import IMAPClient


if __name__ == "__main__":
    logging.basicConfig(
        format="%(asctime)s|%(levelname)s|%(filename)s|%(funcName)s||%(message)s",
        level=logging.INFO,
        datefmt="%H:%M:%S",
    )

    logging.info("STARTING")

    server = IMAPClient("imap.seznam.cz")
    server.login(USERNAME, PASSWORD)

    select_info = server.select_folder("INBOX")
    print(select_info)

    messages = server.search("UNSEEN")
    server.fetch(messages, "RFC822")

    logging.info("FINISHED")
