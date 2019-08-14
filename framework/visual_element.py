from selenium.common.exceptions import NoSuchElementException


class VisualElement:

    def __init__(self, driver, accessibility_id=None, name=None, xpath=None):
        self.__driver = driver
        self.__accessibility_id = accessibility_id
        self.__name = name
        self.__xpath = xpath

    def get(self):
        element_found = None
        if self.__xpath is not None:
            try:
                element_found = self.__driver.find_element_by_xpath(self.__xpath)
            except NoSuchElementException:
                return None
        if self.__name is not None:
            try:
                element_found = self.__driver.find_element_by_name(self.__name)
            except NoSuchElementException:
                return None
        if self.__accessibility_id is not None:
            try:
                element_found = self.__driver.find_element_by_accessibility_id(self.__accessibility_id)
            except NoSuchElementException:
                return None
        assert element_found is not None
        return element_found
