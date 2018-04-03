from GameFrame import RoomObject, Globals
import pygame


class TitleText(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        image = self.load_image('header.png')
        self.set_image(image, 800, 100)

        self.handle_key_events = True

    def key_pressed(self, key):
        if key[pygame.K_ESCAPE]:
            self.room.running = False
            self.room.quitting = True
            Globals.running = False
        if key[pygame.K_UP]:
            self.room.selection_prev()
        elif key[pygame.K_DOWN]:
            self.room.selection_next()
        if key[pygame.K_RETURN]:
            self.room.select()
