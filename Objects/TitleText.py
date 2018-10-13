from GameFrame import RoomObject, Globals
import pygame


class TitleText(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        self.selectable = True
        image = self.load_image('header.png')
        self.set_image(image, 800, 100)

        self.handle_key_events = True

    def key_pressed(self, key):
        if key[pygame.K_ESCAPE]:
            self.room.running = False
            self.room.quitting = True
            Globals.running = False
        if key[pygame.K_UP]:
            if self.selectable:
                self.room.selection_prev()
                self.selectable = False
                self.set_timer(12, self.set_selectable)
        elif key[pygame.K_DOWN]:
            if self.selectable:
                self.room.selection_next()
                self.selectable = False
                self.set_timer(12, self.set_selectable)
        if key[pygame.K_RETURN]:
            self.room.select()

    def set_selectable(self):
        self.selectable = True
