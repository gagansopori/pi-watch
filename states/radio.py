import vlc
from .base import State
from radio_channels import RADIO_CHANNELS

class RadioState(State):
    def __init__(self, context):
        super().__init__(context)
        self.current_channel_index = 0
        self.player = vlc.MediaPlayer()

    def enter(self):
        self.context.set_button_callback('A', self.volume_up)
        self.context.set_button_callback('B', self.volume_down)
        self.context.set_button_callback('X', self.next_channel)
        self.context.set_button_callback('Y', self.exit_radio)

        self.play_channel()

    def play_channel(self):
        url = RADIO_CHANNELS[self.current_channel_index]
        self.player.set_mrl(url)
        self.player.play()
        self.context.display_radio_channel(url)

    def volume_up(self):
        vol = self.player.audio_get_volume()
        self.player.audio_set_volume(min(vol + 10, 100))

    def volume_down(self):
        vol = self.player.audio_get_volume()
        self.player.audio_set_volume(max(vol - 10, 0))

    def next_channel(self):
        self.current_channel_index = (self.current_channel_index + 1) % len(RADIO_CHANNELS)
        self.play_channel()

    def exit_radio(self):
        self.player.stop()
        from .clock import ClockState
        self.context.change_state(ClockState(self.context))
