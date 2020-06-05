#!/usr/bin/env python

"""
Only Python core libraries
"""

import logging
import imaplib

if __name__ == "__main__":
    logging.basicConfig(
        format="%(asctime)s|%(levelname)s|%(filename)s|%(funcName)s||%(message)s",
        level=logging.INFO,
        datefmt="%H:%M:%S",
    )

    logging.info("STARTING")

    server = imaplib.IMAP4_SSL("imap.seznam.cz")
    server.login(USERNAME, PASSWORD)
    server.select("INBOX")

    typ, data = server.search(None, "UNSEEN")
    for num in data[0].split():
        typ, data = server.fetch(num, "(RFC822)")
        print(typ)
        print(data)

    server.close()
    server.logout()

    logging.info("FINISHED")
