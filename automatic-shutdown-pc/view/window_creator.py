#!/usr/bin/env python

import PySimpleGUI as sg


class WindowCreator:
    def __init__(self, model):
        self.model = model
        self.frames = []

    def create(self):
        return self._create_ui_window()

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
            size=(360, 340),
            element_justification="center",
            font="Any 12",
            finalize=True,
        )

        self._expand_all_frames()

        # radio_group = window.Element("radio_tasks_id")
        # self._select_first_radio_item(radio_group)

        return window

    def _create_tasks_frame(self):
        tasks = self.model.get_tasks()
        radio_group = self._create_tasks_radio_group(tasks)

        return self._create_frame("Vyberte akci", [radio_group])

    def _create_frame(self, title, layout):
        frame = sg.Frame(
            title=title, layout=layout, font="Any 16", element_justification="center",
        )
        self.frames.append(frame)
        return frame

    def _create_tasks_radio_group(self, tasks):
        radio_group_id = "radio_tasks_id"
        radio_group = []

        default = True
        for task in tasks:
            radio_item = sg.Radio(
                text=task.get_name(),
                group_id=radio_group_id,
                key=f"radio_{task.get_name()}",
                tooltip=task.get_description(),
                enable_events=True,
                default=default,
            )
            if default:
                default = False

            radio_group.append(radio_item)
        return radio_group

    def _select_first_radio_item(self, radio_group):
        for radio_item in radio_group:
            radio_item.update(value=True)

    def _create_timing_frame(self):
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

        onehour_in_minutes = 60
        twelvehours_in_minutes = 12 * onehour_in_minutes

        sequence = []
        for i in range(0, twelvehours_in_minutes, minutes_step):
            hour_part = i // onehour_in_minutes  # integer division
            minute_part = i % onehour_in_minutes  # mod
            sequence.append(f"{hour_part:02}:{minute_part:02}")

        return sequence

    def _create_countdown_frame(self):
        layout = [
            [
                sg.Text(text="Kdy vyprší:", auto_size_text=True),
                sg.Text(
                    text="00:00",
                    key="text_countdown_when_elapsed",
                    font="Any 14",
                    auto_size_text=True,
                ),
                sg.Text(text="Za jak dlouho:", auto_size_text=True),
                sg.Text(
                    text="00:00",
                    key="text_countdown_remaining",
                    font="Any 14",
                    auto_size_text=True,
                ),
            ]
        ]

        return self._create_frame("Odpočet", layout)

    def _create_controls_frame(self):

        layout = [
            [
                sg.Button(button_text="Spustit", key="button_submit"),
                sg.Button(button_text="Zrušit", key="button_cancel"),
                sg.Button(button_text="Exit", key="button_exit"),
            ]
        ]

        return self._create_frame("Ovládání", layout)

    def _expand_all_frames(self):
        for frame in self.frames:
            frame.expand(expand_x=True, expand_y=False, expand_row=False)

    def _create_statusbar_frame(self):

        layout = [[sg.StatusBar(text="Vyberte a načasujte akci.", key="status_bar")]]

        return self._create_frame("StatusBar", layout)
