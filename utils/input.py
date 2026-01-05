from .position import Position

class Input:
    start_pos = Position(0, 0)
    end_pos = Position(0, 0)

    @staticmethod
    def on_click(event):
        Input.start_pos = Position(event.x, event.y)

    @staticmethod
    def on_release(event):
        Input.end_pos = Position(event.x, event.y)