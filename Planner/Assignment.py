import datetime
# import pytz


class Assignment:
    def __init__(self, name: str, category: str = None, start_datetime: datetime.datetime = None, due_datetime: datetime.datetime = None, notes: str = None, difficulty: int = None) -> None:
        self._name = name
        self._category = category
        self._start_datetime = start_datetime
        self._due_datetime = due_datetime
        self._notes = notes
        self._difficulty = difficulty

    def set_name(self, name: str) -> None:
        self._name = name

    def get_name(self) -> str:
        return self._name

    def set_category(self, category: str) -> None:
        self._category = category

    def get_category(self) -> str:
        return self._category

    def set_start_datetime(self, start_date: datetime.datetime) -> None:
        self._start_datetime = start_date

    def get_start_datetime(self) -> datetime.datetime:
        return self._start_datetime

    def set_due_datetime(self, due_date: datetime.datetime) -> None:
        self._due_datetime = due_date

    def get_due_datetime(self) -> datetime.datetime:
        return self._due_datetime

    def set_notes(self, notes: str) -> None:
        self._notes = notes

    def get_notes(self) -> str:
        return self._notes

    def set_difficulty(self, difficulty: int) -> None:
        self._difficulty = difficulty

    def get_difficulty(self) -> int:
        return self._difficulty

    def get_time_until_start(self) -> datetime.timedelta:
        return self._start_datetime - datetime.datetime.now()

    def get_time_until_due(self) -> datetime.timedelta:
        return self._due_datetime - datetime.datetime.now()

    def styled_string(self) -> str:
        return f'{self._name}: (Category: {self._category}) [Difficulty: {self._difficulty}]\n\t{self._start_datetime.strftime("%m/%d/%Y(%H:%M)")} -- {self._due_datetime.strftime("%m/%d/%Y(%H:%M)")}\n\tNotes: {self._notes}'

    def __str__(self) -> str:
        return f'{self._name};{self._category};{self._start_datetime.strftime("%m/%d/%Y(%H:%M)")};{self._due_datetime.strftime("%m/%d/%Y(%H:%M)")};{self._notes};{self._difficulty}'
