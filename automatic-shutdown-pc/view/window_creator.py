#!/usr/bin/env python

import PySimpleGUI as sg
import os


class WindowCreator:
    """
    Instantiate app's UI
    This class will create and return PySimpleGui window object
    """

    WINDOW_X = 360
    WINDOW_Y = 390
    WINDOW_ICO_FILE = os.path.join("resources", "shutdown_icon.ico")
    ERROR_ICO_FILE = os.path.join("resources", "error_icon2.ico")

    def __init__(self, tasks):
        self.tasks = tasks
        self.frames = []

    def create(self):
        return self._create_ui_window()

    def create_error_popup(self, error_message):
        return sg.popup_error(
            error_message,
            title="ERROR",
            non_blocking=False,
            grab_anywhere=True,
            icon=WindowCreator.ERROR_ICO_FILE,
            keep_on_top=True,
            line_width=200,
        )

    def _create_ui_window(self):
        sg.ChangeLookAndFeel("GreenTan")

        layout = [
            [self._create_tasks_frame()],
            [self._create_timing_frame()],
            [self._create_countdown_frame()],
            [self._create_controls_frame()],
            [self._create_statusbar_frame()],
        ]

        window = sg.Window(
            title="Automatické vypnutí PC",
            layout=layout,
            size=(WindowCreator.WINDOW_X, WindowCreator.WINDOW_Y),
            element_justification="center",
            font="Any 12",
            finalize=True,
            default_button_element_size=(8, 1),
            icon=WindowCreator.WINDOW_ICO_FILE,
        )

        self._expand_all_frames()

        return window

    ###########################################################################

    def _create_tasks_frame(self):
        """Choose task - operation"""
        tasks_names = self._get_tasks_names(self.tasks)

        layout = [
            [self._create_tasks_combo(tasks_names)],
            [
                sg.Text("Parametr: "),

                sg.Input(
                    tooltip="Vložte požadovanou hodnotu parametru akce.",
                    key="input_parameter",
                )
            ]
        ]

        return self._create_frame("Vyberte akci", layout)

    def _get_tasks_names(self, tasks):
        tasks_names = []
        for task in tasks:
            tasks_names.append(task.get_name())
        return tasks_names

    def _create_tasks_combo(self, tasks_names):
        default_value = tasks_names[0]

        return sg.Combo(
            values=tasks_names,
            default_value=default_value,
            key="combo_tasks",
            enable_events=True,
        )

    def _create_frame(self, title, layout):
        frame = sg.Frame(
            title=title,
            layout=layout,
            font="Any 16",
            element_justification="center",
            size=(WindowCreator.WINDOW_X - 10, WindowCreator.WINDOW_Y - 5),
        )
        self.frames.append(frame)
        return frame

    ###########################################################################

    def _create_timing_frame(self):
        """Schedule task - choose timedelta"""
        step_in_minutes = 15
        sequence = self._generate_time_sequence(step_in_minutes)
        initial_value = sequence[2]
        layout = [
            [
                sg.Spin(
                    values=sequence,
                    initial_value=initial_value,
                    key="spin_timing",
                    size=(5, 2),
                    enable_events=True,
                )
            ]
        ]

        return self._create_frame("Načasujte", layout)

    def _generate_time_sequence(self, minutes_step=15):
        """Generate sequence: 00:00, 00:15, 00:30, ... 11:45"""

        onehour_in_minutes = 60
        twelvehours_in_minutes = 12 * onehour_in_minutes

        sequence = []
        for i in range(0, twelvehours_in_minutes, minutes_step):
            hour_part = i // onehour_in_minutes  # integer division
            minute_part = i % onehour_in_minutes  # mod
            sequence.append(f"{hour_part:02}:{minute_part:02}")

        return sequence

    ###########################################################################

    def _create_countdown_frame(self):
        """When action is scheduled, the countdown will be ticking..."""
        layout = [
            [
                sg.Text(text="Kdy vyprší:", auto_size_text=True),
                sg.Text(
                    text="00:00",
                    key="text_countdown_when_elapsed",
                    font="Any 14",
                    auto_size_text=True,
                ),
            ],
            [
                sg.Text(text="Za jak dlouho:", auto_size_text=True),
                sg.Text(
                    text="00:00:00",
                    key="text_countdown_remaining",
                    font="Any 14",
                    auto_size_text=True,
                ),
            ],
        ]

        return self._create_frame("Odpočet", layout)

    ###########################################################################

    def _create_controls_frame(self):
        """Buttons, buttons, buttons..."""

        layout = [
            [
                sg.Button(button_text="Spustit", key="button_submit", size=(8, 1)),
                sg.Button(button_text="Zrušit", key="button_cancel", size=(8, 1)),
                sg.Button(button_text="Exit", key="button_exit", size=(8, 1)),
            ]
        ]

        return self._create_frame("Ovládání", layout)

    ###########################################################################

    def _expand_all_frames(self):
        """
        PySimpleGui's Frame object is sized based on elements it contains...
        This will expand frames to the size of the window object...
        """
        for frame in self.frames:
            frame.expand(expand_x=True, expand_y=False, expand_row=False)

    ###########################################################################

    def _create_statusbar_frame(self):
        """To inform user about what is happening in the application"""
        layout = [
            [
                sg.StatusBar(
                    text="Vyberte a načasujte akci.",
                    key="status_bar",
                    size=(WindowCreator.WINDOW_X - 25, 1),
                )
            ]
        ]

        return self._create_frame("StatusBar", layout)
