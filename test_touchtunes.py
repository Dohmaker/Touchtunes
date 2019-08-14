import unittest
from framework.click_action import ClickAction
from framework.appium_test_case import AppiumTestCase
from time import sleep


class TestClass(AppiumTestCase):

    def test_scenario_1_onboarding(self):
        self.onboarding()
        self.assertIsNotNone(self.visualElements.bell_button.get(), "You have not reached the main page!")

    def test_scenario_2_Play_song(self):
        self.onboarding()
        # the scrolling is a hack due to lack of properly identified items in the app
        for x in range(0, 4):
            self.scroll_down()
        self.scroll_up()
        for x in range(0, 3):
            self.scroll_right()
        ClickAction(self.visualElements.last_editorial_pick).execute()
        sleep(2)
        ClickAction(self.visualElements.play_pause_button).execute()
        # Asserting the playing music requires either the play and pause button to be identified or applitool being used
        sleep(2)
        self.assertEqual(self.visualElements.current_song.get().text,'Photo', 'The song Photo is not playing!')
        ClickAction(self.visualElements.home_screen).execute()
        sleep(2)
        # Scroll up to display the top menu in order to identify if we are in the main menu
        self.assertIsNotNone(self.visualElements.left_menu_button.get(), "You have not reached the main page!")

    def onboarding(self):
        # sleep the splash page away
        sleep(6)
        self.assertIsNotNone(self.visualElements.onboarding_icon.get(), "The onboarding page has not been reached")
        ClickAction(self.visualElements.hindi_button).execute()
        self.scroll_down()
        ClickAction(self.visualElements.assamese_button).execute()
        #Even though the button updates automatically the source has a problem updating quickly for the text being asserted
        sleep(6)
        self.assertEqual(self.visualElements.selected_items.get().text, '1 Selected', 'No items where selected!')
        ClickAction(self.visualElements.done_button).execute()
        if self.visualElements.ad_close_button.get() is not None:
            ClickAction(self.visualElements.ad_close_button).execute()


    def scroll_down(self):
        self.driver.swipe(470, 1400, 470, 300, 400)
        sleep(1)


    def scroll_up(self):
        self.driver.swipe(470, 300, 470, 1400, 1100)
        sleep(1)


    def scroll_right(self):
        self.driver.swipe(1000, 400, 100, 400, 400)
        sleep(1)

if __name__ == '__main__':
    unittest.main()
