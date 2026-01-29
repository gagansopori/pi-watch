from .base import State

class ClockState(State):
    def enter(self):
        self.context.display_clock()
        self.context.set_button_callback('A', self.goto_radio)

    def update(self):
        self.context.display_clock()

    def goto_radio(self):
        from .radio import RadioState
        self.context.change_state(RadioState(self.context))
