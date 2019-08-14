from action import Action
from time import sleep


class ClickAction(Action):
    def __init__(self, visual_element, sleep_time=0):
        self.__visual_element = visual_element
        self.__sleep = sleep_time

    def execute(self):
        self.__visual_element.get().click()
        sleep(self.__sleep)
        return 1
