import RPi.GPIO as GPIO

from src.constants.BoardConstants import BUTTONS, LABELS


class CreateBoardControls:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(BUTTONS, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def handle_action(self, pin):
        label = LABELS[BUTTONS.index(pin)]
        if pin == LABELS[BUTTONS.index(pin)]:
            print("Button press detected on pin: {} label: {}".format(pin, label))

        # This will represent a Finite State Automaton.
        if label == 'A':
            '''
            Pressing 'A' will clear the current state & enter the set-alarm state. A new screen & control-set will be 
            loaded onto the display. The flow will trigger as follows:
            1. The new screen will show hours, with current hr as default.
            2. The new set of controls will be as follows
                - A = Prev, X = Next, B = Set, Y = Cancel
            3. Pressing A & X will shift the hrs, up or down respectively.
            4. B will save the hr, & transition the state to mins. During this the control-set will remain the same.
            5. Y will change the current state back to the original state of machine.
            '''
        if label == 'B':
            '''
            Pressing 'B' will change the state of the machine to display the system-ops. A new screen & control set will
            be loaded onto the display. The flow will be as:
            1. The new screen will show 4 system operations with their triggers as follows:
                - A: System Shutdown
                    - Pressing A will shutdown the system.
                - B: System Reboot 
                    - Pressing B will reboot the system.
                - C: CPU Metrics 
                    - CPU & Memory Usage, CPU Temp & HDD Space
                    - Pressing X will enter this state & display cpu metrics.
                - D: Network Metrics
                    - Host-IP, SSID & Network Speed (Possibly)
                    - Pressing Y will enter this state & display network metrics.
            2. The states A & B will be triggered instantaneously.
            3. By Default, states C & D will remain active for 10s, before transitioning to default state.
            4. When in state C, Pressing Y will trigger a transition to the default state.
            5. When in state D, Pressing Y will trigger a transition to the default state.
            '''
#         if label == 'X':
#             print("Do Something for X")
#         if label == 'Y':
#             print("Do Something for Y")
