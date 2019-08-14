class Action:
    def __init__(self, visual_element=None):
        self.__visual_element = visual_element

    def execute(self):
        raise Exception("Not defined")
