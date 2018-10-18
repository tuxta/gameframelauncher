from GameFrame import RoomObject, Globals
import pygame


class TitleText(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        self.selectable = True
        image = self.load_image('header.png')
        self.set_image(image, 800, 100)

        self.handle_key_events = True
        self.can_select = True

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
            if self.can_select:
                self.can_select = False
                self.room.select()

    def joy_pad_signal(self, p1_buttons, p2_buttons):
        if p1_buttons[10] or p2_buttons[10]:
            self.room.running = False
            self.room.quitting = True
            Globals.running = False
        if p1_buttons[0] or p2_buttons[0]:
            if self.selectable:
                self.room.selection_prev()
                self.selectable = False
                self.set_timer(12, self.set_selectable)
        elif p1_buttons[2] or p2_buttons[2]:
            if self.selectable:
                self.room.selection_next()
                self.selectable = False
                self.set_timer(12, self.set_selectable)
        if p1_buttons[4] or p2_buttons[4]:
            if self.can_select:
                self.can_select = False
                self.room.select()

    def set_selectable(self):
        self.selectable = True
