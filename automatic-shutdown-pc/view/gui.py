#!/usr/bin/env python

import logging
import PySimpleGUI as sg


class Gui:
    """A UI defined using PySimpleGUI library"""

    def __init__(self, model):
        self.model = model
        self.window = self._create_ui_window()

    def _create_ui_window(self):
        sg.ChangeLookAndFeel("GreenTan")
        self._create_tasks_frame()

    def _create_tasks_frame(self):
        return (
            sg.Frame(
                "Vyberte Akci",
                [
                    [
                        sg.Slider(
                            range=(1, 100),
                            orientation="v",
                            size=(5, 20),
                            default_value=25,
                            tick_interval=25,
                        ),
                        sg.Slider(
                            range=(1, 100),
                            orientation="v",
                            size=(5, 20),
                            default_value=75,
                        ),
                        sg.Slider(
                            range=(1, 100),
                            orientation="v",
                            size=(5, 20),
                            default_value=10,
                        ),
                        sg.Col(column1),
                    ]
                ],
            ),
        )

    def _create_timing_frame(self):
        pass

    def _create_countdown_frame(self):
        pass

    def _create_controls_frame(self):
        pass

    def _create_statusbar_frame(self):
        pass

    def run(self):
        while True:
            event, values = self.window.Read(timeout=100)

            if event is None or event == "Exit":
                break
            elif event.startswith("b_load_"):
                pass

        self.window.Close()
