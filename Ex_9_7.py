from datetime import datetime
#import time

class Case:
    def __init__(self, case_: dict) -> None:
        self.case_ = case_
    def retrieve_seconds(self) -> None:
        if self.case_['end_task'] is None:
            print("Task not finished yet")
        else:
            element_created_task = datetime.strptime(self.case_['created_task'][:-3], ("%Y-%m-%dT%H:%M:%S+%f"))
            element_end_task = datetime.strptime(self.case_['end_task'][:-3], ("%Y-%m-%dT%H:%M:%S+%f"))
            print(element_end_task.timestamp()-element_created_task.timestamp())

def main():
    first_case = {
        'name': 'first_case',
        'created_task': '2021-10-26T19:48:12+00:00',
        'end_task': None
    }
    second_case = {
        'name': 'second_case',
        'created_task': '2021-09-26T19:48:12+00:00',
        'end_task': '2021-10-26T19:48:12+00:00'
    }
    test_case = {
        'name': 'second_case',
        'created_task': '2021-09-26T19:48:12+00:00',
        'end_task':     '2021-09-27T19:48:12+00:00'
    }

    case1 = Case(first_case)
    case1.retrieve_seconds()
    case2 = Case(second_case)
    case2.retrieve_seconds()

    #test 1 day = 24*60*60 = 86400
    case3 = Case(test_case)
    case3.retrieve_seconds()


if __name__ == "__main__":
    main()
