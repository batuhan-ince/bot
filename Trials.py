from __future__ import division
from asciimatics.effects import Wipe, Print
from asciimatics.renderers import FigletText, SpeechBubble
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError
import sys


def demo(screen):
    scenes = []

    effects = [
        Wipe(screen, bg=Screen.COLOUR_RED, stop_frame=screen.height * 2 + 30),
        Print(screen, FigletText("WOLOOLO", "epic"), screen.height // 2 - 4,
              colour=7 - Screen.COLOUR_RED,
              bg=Screen.COLOUR_RED,
              start_frame=screen.height * 2),
        Print(screen,
              SpeechBubble("Testing background colours - press X to exit"),
              screen.height-5,
              speed=1, transparent=False)
    ]
    scenes.append(Scene(effects, 0, clear=False))

    screen.play(scenes, stop_on_resize=True)


if __name__ == "__main__":
    while True:
        try:
            Screen.wrapper(demo)
            sys.exit(0)
        except ResizeScreenError:
            pass