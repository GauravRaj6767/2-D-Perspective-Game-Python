from kivy.uix.relativelayout import RelativeLayout


def keyboard_closed(self):
    self.keyboard.unbind(on_key_down=self.on_keyboard_down)
    self.keyboard.unbind(on_key_up=self.on_keyboard_up)
    self.keyboard = None


def on_keyboard_down(self, keyboard, keycode, text, modifiers):
    if keycode[1] == 'left' or keycode[1] == 'a':
        self.current_speed_x = self.SPEED_X
    elif keycode[1] == 'right' or keycode[1] == 'd':
        self.current_speed_x = -self.SPEED_X

    return True


def on_keyboard_up(self, keyboard, keycode):
    self.current_speed_x = 0
    return True


def on_touch_up(self, touch):
    # print("UP")
    self.current_speed_x = 0


def on_touch_down(self, touch):
    if not self.state_game_over and self.state_game_started :
        if touch.x < self.width / 2:
            # print("left")
            self.current_speed_x = self.SPEED_X

        else:
            # print("right")
            self.current_speed_x = -self.SPEED_X

    return super(RelativeLayout, self).on_touch_down(touch)
