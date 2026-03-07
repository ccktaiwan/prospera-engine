class ProsperaEngine:

    def __init__(self):

        self.state = "INIT"

        self.transitions = {
            ("INIT", "BOOT"): "RUNNING",
            ("RUNNING", "STOP"): "HALTED"
        }

    def emit(self, event):

        key = (self.state, event)

        if key not in self.transitions:
            raise Exception(f"Invalid transition: {self.state} + {event}")

        new_state = self.transitions[key]

        print(f"{self.state} -> {new_state}")

        self.state = new_state

        return self.state


if __name__ == "__main__":

    engine = ProsperaEngine()

    engine.emit("BOOT")
    engine.emit("STOP")
