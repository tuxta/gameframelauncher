from GameFrame import TextObject


class GameButtonText(TextObject):
    def __init__(self, room, x, y, text, game_title, font_size):
        TextObject.__init__(self, room, x, y, text, font_size, 'LiberationMono', (255, 255, 255))

        self.game_title = game_title

    def selected(self):
        self.room.run_game(self.game_title)

    def increase_size(self):
        self.size += 5
        self.update_text()

    def decrease_size(self):
        self.size -= 5
        self.update_text()
