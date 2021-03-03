from mycroft import MycroftSkill
from mycroft.skills import resting_screen_handler


class GezHomescreen(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @resting_screen_handler("Gez's personal homescreen")
    def handle_homescreen_gez(self, message):
        self.gui.clear()
        halloween_img = "https://mycroft.ai/wp-content/uploads/2019/02/haloween-Mark-I.png"
        self.gui.show_image(halloween_img)


def create_skill():
    return GezHomescreen()

