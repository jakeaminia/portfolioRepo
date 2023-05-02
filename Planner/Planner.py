from Assignment import Assignment
from collections.abc import Iterable
import datetime


class Planner:
    def __init__(self, name: str, assignments_dict: dict = None) -> None:
        self._name = name
        if assignments_dict:
            self._assignments_dict = assignments_dict
        else:
            self._assignments_dict = dict()

    def set_name(self, name: str) -> None:
        self._name = name

    def get_name(self) -> str:
        return self._name

    def get_assignment(self, name: str) -> Assignment:
        return self._assignments_dict.get(name, None)

    def add_assignment(self, assignment: Assignment) -> None:
        self._assignments_dict[assignment.get_name()] = assignment

    def add_assignments(self, *assignments: Assignment) -> None:
        for assignment in assignments:
            self.add_assignment(assignment)

    def parse_assignment(self, assignment_string: str) -> None:
        name, category, start_datetime, due_datetime, notes, difficulty = assignment_string.strip().split(';')

        if start_datetime[-1] != ')':
            start_datetime = f'{start_datetime}(8:30)'
        if due_datetime[-1] != ')':
            due_datetime = f'{due_datetime}(23:59)'

        new_assignment = Assignment(name.strip(), category.strip(
        ), datetime.datetime.strptime(start_datetime, '%m/%d/%Y(%H:%M)'), datetime.datetime.strptime(due_datetime, '%m/%d/%Y(%H:%M)'), notes, int(difficulty))
        self.add_assignment(new_assignment)

    def parse_assignments(self, assignment_strings: Iterable[str]) -> None:
        for assignment_string in assignment_strings:
            self.parse_assignment(assignment_string)

    def parse_assignments_from_file(self, file_name: str) -> None:
        with open(file_name, 'r') as file:
            self.parse_assignments(file.readlines())

    def remove_assignment(self, name: str) -> bool:
        if name in self._assignments_dict:
            del self._assignments_dict[name]
            return True
        return False

    def change_assignment_name(self, old_assignment_name: str, new_assignment_name: str) -> bool:
        if new_assignment_name in self._assignments_dict or old_assignment_name not in self._assignments_dict:
            return False
        assignment: Assignment = self._assignments_dict.pop(
            old_assignment_name)
        self._assignments_dict[new_assignment_name] = assignment
        assignment.set_name(new_assignment_name)
        return True

    def get_assignments_as_list(self) -> list:
        return list(self._assignments_dict.values())

    def get_assignments_as_sorted_list(self, parameter: str, sort_descending: bool, destination_file_name: str = None):
        sorting_lambda = None
        match parameter.lower():
            case 'name':
                def sorting_lambda(x): return x.get_name()
            case 'category':
                def sorting_lambda(x): return x.get_category()
            case 'start_datetime':
                def sorting_lambda(x): return x.get_start_datetime()
            case 'due_datetime':
                def sorting_lambda(x): return x.get_due_datetime()
            case 'notes':
                def sorting_lambda(x): return x.get_notes()
            case 'difficulty':
                def sorting_lambda(x): return x.get_difficulty()

        result = sorted(self.get_assignments_as_list(),
                        key=sorting_lambda, reverse=sort_descending)
        if not destination_file_name:
            return result

        with open(destination_file_name, 'w') as file:
            for assignment in result:
                # print(assignment)
                file.write(
                    f'{str(assignment)}\n')

    def __str__(self) -> str:
        return f'{self._name} ({len(self)})'

    def __sizeof__(self) -> int:
        return len(self._assignments_dict)
