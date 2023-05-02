from Assignment import Assignment
from Planner import Planner
# import datetime


def new_test():
    source_text_file_name = './assignments.txt'
    destination_text_file_name = './result_assignments.txt'

    source_text_file_name, destination_text_file_name = destination_text_file_name, source_text_file_name

    new_planner: Planner = Planner('New Planner')

    new_planner.parse_assignments_from_file(source_text_file_name)
    new_planner.get_assignments_as_sorted_list(
        'name', False, destination_text_file_name)


def old_test():
    # test_planner: Planner = Planner('Test Planner')
    # first_assignment: Assignment = Assignment('Eat Cake', 'To-Do', datetime.datetime(
    #     year=2023, month=5, day=1, hour=15, minute=30), datetime.datetime(year=2023, month=5, day=12, hour=15, minute=30), 'make sure it\'s yummy!')
    # second_assignment: Assignment = Assignment('TWD Essay', 'Class', datetime.datetime(
    #     year=2023, month=5, day=1, hour=15, minute=30), datetime.datetime(year=2023, month=5, day=7, hour=12), 'remember to save the recordings')
    # third_assignment: Assignment = Assignment('W', 'W', datetime.datetime(
    #     year=2023, month=5, day=1, hour=15, minute=30), datetime.datetime(year=2023, month=6, day=30, hour=9, minute=24), 'W')
    # test_planner.add_assignments(
    #     first_assignment, second_assignment, third_assignment)
    # assignment_list: list = test_planner.get_assignments_as_sorted_list(
    #     'name', False)
    # for element in assignment_list:
    #     print(f'{element}\n- - - - - - - - - - -')
    pass


new_test()
