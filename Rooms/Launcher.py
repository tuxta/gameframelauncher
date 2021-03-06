from GameFrame import Level, Globals
from Objects import GameButtonText, TitleText

import os
import pygame
import subprocess


class Launcher(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        self.set_background_image('background.png')
        self.games = []
        self.curr_selection = 0

        self.title = TitleText(self, 0, 0)
        self.add_room_object(self.title)

        curr_y_pos = 275
        font_size = 60
        for game in Globals.game_list:
            game_button = GameButtonText(self, 40, curr_y_pos, game[0], game[1], font_size)
            font_size -= 10
            curr_y_pos += 60
            self.add_room_object(game_button)
            self.games.append(game_button)
        self.games[0].colour = (0, 0, 0)
        self.games[0].update_text()

    def run_game(self, game_title):
        pygame.display.toggle_fullscreen()
        # Move to the Game Directory #
        os.chdir(os.path.join("Games", game_title))

        # Close off the JoySticks
        for i in range(len(self.joysticks)):
            self.joysticks[i].quit()
            
        # Launch the Game #
        subprocess.run(["python3", "MainController.py"])

        # Clear Events and Button Clicks #
        pygame.event.clear()
        for i in range(len(self.p1_btns)):
            self.p1_btns[i] = 0
        for i in range(len(self.p2_btns)):
            self.p2_btns[i] = 0

        for i in range(len(self.joysticks)):
            self.joysticks[i].init()
        
        # Move back to the original directory
        os.chdir(os.path.join('..', '..'))
        pygame.display.toggle_fullscreen()
        
        pygame.event.clear()

    def selection_prev(self):
        self.title.can_select = True
        if self.curr_selection > 0:
            for index, game in enumerate(self.games):
                game.y += 60
                if index < self.curr_selection:
                    game.increase_size()
                else:
                    game.decrease_size()
            self.games[self.curr_selection].colour = (255, 255, 255)
            self.games[self.curr_selection].update_text()
            self.curr_selection -= 1
            self.games[self.curr_selection].colour = (0, 0, 0)
            self.games[self.curr_selection].update_text()

    def selection_next(self):
        self.title.can_select = True
        if self.curr_selection < len(self.games) - 1:
            for index, game in enumerate(self.games):
                game.y -= 60
                if index > self.curr_selection:
                    game.increase_size()
                else:
                    game.decrease_size()
            self.games[self.curr_selection].colour = (255, 255, 255)
            self.games[self.curr_selection].update_text()
            self.curr_selection += 1
            self.games[self.curr_selection].colour = (0, 0, 0)
            self.games[self.curr_selection].update_text()

    def select(self):
        self.games[self.curr_selection].selected()
