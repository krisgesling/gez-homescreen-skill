from mycroft import MycroftSkill
from mycroft.skills import resting_screen_handler


class PersonalHomescreen(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @resting_screen_handler("Personalised homescreen")
    def handle_homescreen(self, message):
        halloween_img = "https://mycroft.ai/wp-content/uploads/2019/02/haloween-Mark-I.png"
        background_img = self.settings.get("background_img", halloween_img)
        self.gui.show_image(background_img)


def create_skill():
    return PersonalHomescreen()

