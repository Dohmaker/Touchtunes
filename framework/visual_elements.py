from visual_element import VisualElement


class VisualElements:
    def __init__(self, driver):
        # Creates dictionary of all currently used buttons in the app
        # Left menu buttons
        self.onboarding_icon = VisualElement(driver, xpath='/hierarchy/android.widget.FrameLayout/android.widget.'
                                                           'LinearLayout/android.widget.FrameLayout/android.widget.'
                                                           'LinearLayout/android.widget.FrameLayout/android.widget.'
                                                           'FrameLayout/android.support.v4.widget.DrawerLayout/android.'
                                                           'widget.RelativeLayout/android.view.ViewGroup/android.widget'
                                                           '.FrameLayout/android.widget.FrameLayout/android.widget'
                                                           '.LinearLayout/android.widget.ListView/android.widget.'
                                                           'RelativeLayout/android.widget.LinearLayout/android.widget'
                                                           '.ScrollView/android.widget.LinearLayout/android.widget'
                                                           '.RelativeLayout/android.widget.ImageView')
        self.hindi_button = VisualElement(driver, xpath='hierarchy/android.widget.FrameLayout/android.widget.'
                                                        'LinearLayout/android.widget.FrameLayout/android.widget.'
                                                        'LinearLayout/android.widget.FrameLayout/android.widget.'
                                                        'FrameLayout/android.support.v4.widget.DrawerLayout/android.'
                                                        'widget.RelativeLayout/android.view.ViewGroup/android.widget.'
                                                        'FrameLayout/android.widget.FrameLayout/android.widget.'
                                                        'LinearLayout/android.widget.ListView/android.widget.'
                                                        'RelativeLayout/android.widget.LinearLayout/android.widget.'
                                                        'ScrollView/android.widget.LinearLayout/android.widget.'
                                                        'LinearLayout[2]/android.widget.RelativeLayout/android.widget.'
                                                        'ImageView[1]')
        self.assamese_button = VisualElement(driver, 'Assamese')
        self.selected_items = VisualElement(driver, xpath='/hierarchy/android.widget.FrameLayout/android.widget.'
                                                          'LinearLayout/android.widget.FrameLayout/android.widget.'
                                                          'LinearLayout/android.widget.FrameLayout/android.widget.'
                                                          'FrameLayout/android.support.v4.widget.DrawerLayout/android.'
                                                          'widget.RelativeLayout/android.view.ViewGroup/android.widget.'
                                                          'FrameLayout/android.widget.FrameLayout/android.widget.'
                                                          'LinearLayout/android.widget.RelativeLayout/android.widget.'
                                                          'TextView')

        self.done_button = VisualElement(driver, xpath= 'hierarchy/android.widget.FrameLayout/android.widget.'
                                                        'LinearLayout/android.widget.FrameLayout/android.widget.'
                                                        'LinearLayout/android.widget.FrameLayout/android.widget.'
                                                        'FrameLayout/android.support.v4.widget.DrawerLayout/android.'
                                                        'widget.RelativeLayout/android.view.ViewGroup/android.widget.'
                                                        'FrameLayout/android.widget.FrameLayout/android.view.'
                                                        'ViewGroup/android.support.v7.widget.RecyclerView/android.'
                                                        'widget.LinearLayout[3]/android.support.v7.widget.'
                                                        'RecyclerView/android.widget.LinearLayout[2]/android.widget.'
                                                        'FrameLayout/android.widget.ImageView')
        self.ad_close_button = VisualElement(driver, 'Interstitial close button')
        self.bell_button = VisualElement(driver, xpath='/hierarchy/android.widget.FrameLayout/android.widget.'
                                                 'LinearLayout/android.widget.FrameLayout/android.widget.'
                                                 'LinearLayout/android.widget.FrameLayout/android.widget.'
                                                 'FrameLayout/android.support.v4.widget.DrawerLayout/android.'
                                                 'widget.RelativeLayout/android.view.ViewGroup[2]/android.widget.'
                                                 'RelativeLayout[2]/android.widget.ImageView')
        self.editorial_picks = VisualElement(driver, xpath='/hierarchy/android.widget.FrameLayout/android.widget.'
                                                     'LinearLayout/android.widget.FrameLayout/android.widget.'
                                                     'LinearLayout/android.widget.FrameLayout/android.widget.'
                                                     'FrameLayout/android.support.v4.widget.DrawerLayout/android.'
                                                     'widget.RelativeLayout/android.view.ViewGroup/android.widget.'
                                                     'FrameLayout[1]/android.widget.FrameLayout/android.view.'
                                                     'ViewGroup/android.support.v7.widget.RecyclerView/android.widget.'
                                                     'LinearLayout[2]/android.widget.TextView')

        self.last_editorial_pick = VisualElement(driver, xpath='/hierarchy/android.widget.FrameLayout/android.widget.'
                                                         'LinearLayout/android.widget.FrameLayout/android.widget.'
                                                         'LinearLayout/android.widget.FrameLayout/android.widget.'
                                                         'FrameLayout/android.support.v4.widget.DrawerLayout/android.'
                                                         'widget.RelativeLayout/android.view.ViewGroup/android.widget.'
                                                         'FrameLayout[1]/android.widget.FrameLayout/android.view.'
                                                         'ViewGroup/android.support.v7.widget.RecyclerView/android.'
                                                         'widget.LinearLayout[1]/android.support.v7.widget.'
                                                         'RecyclerView/android.widget.LinearLayout[4]/android.widget.'
                                                         'FrameLayout')

        self.home_screen = VisualElement(driver, xpath='/hierarchy/android.widget.FrameLayout/android.widget.'
                                                 'LinearLayout/android.widget.FrameLayout/android.widget.'
                                                 'LinearLayout/android.widget.FrameLayout/android.widget.'
                                                 'FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.'
                                                 'RelativeLayout/android.widget.FrameLayout/android.widget.'
                                                 'LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.'
                                                 'ImageView')
        self.left_menu_button = VisualElement(driver, xpath="/hierarchy/android.widget.FrameLayout/android.widget."
                                                      "LinearLayout/android.widget."
                                                      "FrameLayout/android.widget."
                                                      "LinearLayout/android.widget.FrameLayout/android.widget."
                                                      "FrameLayout/android.support.v4.widget.DrawerLayout/android."
                                                      "widget.RelativeLayout/android.view.ViewGroup[2]/android.widget."
                                                      "ImageButton")
        self.play_pause_button = VisualElement(driver, xpath="/hierarchy/android.widget.FrameLayout/android.widget."
                                                             "LinearLayout/android.widget.FrameLayout/android.widget."
                                                             "LinearLayout/android.widget.FrameLayout/android.widget."
                                                             "FrameLayout/android.support.v4.widget.DrawerLayout/"
                                                             "android.widget.RelativeLayout/android.view.ViewGroup[1]/"
                                                             "android.widget.FrameLayout[2]/android.widget."
                                                             "RelativeLayout/android.widget.FrameLayout/android.widget."
                                                             "RelativeLayout/android.widget.LinearLayout/"
                                                             "android.widget.FrameLayout/android.widget."
                                                             "FrameLayout/android.widget.ImageView")

        self.current_song = VisualElement(driver, xpath="/hierarchy/android.widget.FrameLayout/android.widget."
                                                        "LinearLayout/android.widget.FrameLayout/android.widget."
                                                        "LinearLayout/android.widget.FrameLayout/android.widget."
                                                        "FrameLayout/android.support.v4.widget.DrawerLayout/android."
                                                        "widget.RelativeLayout/android.view."
                                                        "ViewGroup[1]/android.widget."
                                                        "FrameLayout[2]/android.widget.RelativeLayout/android.widget."
                                                        "FrameLayout/android.widget.RelativeLayout/android.widget."
                                                        "LinearLayout/android.widget.LinearLayout/android.widget."
                                                        "RelativeLayout[2]/android.widget.LinearLayout/android.widget."
                                                        "TextView[1]")