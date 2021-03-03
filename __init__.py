from mycroft import MycroftSkill, intent_file_handler


class GezHomescreen(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('homescreen.gez.intent')
    def handle_homescreen_gez(self, message):
        self.speak_dialog('homescreen.gez')


def create_skill():
    return GezHomescreen()

