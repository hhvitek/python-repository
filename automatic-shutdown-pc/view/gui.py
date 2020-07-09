#!/usr/bin/env python

import logging
from .window_creator import WindowCreator
from .window_manager import WindowManager


class Gui:
    """A UI defined using PySimpleGUI library"""

    def __init__(self, model):
        self.model = model

        window_creator = WindowCreator(model)
        self.window = window_creator.create()
        self.window_manager = WindowManager(self.window)

    def run(self):
        while True:
            event, values = self.window.Read(timeout=1000, timeout_key="timeout")

            if event is None or event == "Exit" or event == "button_exit":
                break
            elif event == "spin_timing":
                logging.info("Spin changed")
                self.window_manager.spin_timing_changed()
            elif event == "timeout":
                logging.info("Timeout")
            elif event == "button_cancel":
                logging.info("Cancel")
            elif event == "button_submit":
                logging.info("Start")
            else:
                logging.info(event)

        self.window.Close()
