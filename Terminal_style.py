#!/usr/bin/python3
from __future__ import division
from asciimatics.effects import Print
from asciimatics.renderers import ColourImageFile, FigletText, ImageFile, SpeechBubble
from asciimatics.scene import Scene
from asciimatics.event import KeyboardEvent
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError
from asciimatics.paths import DynamicPath
import sys

"""
class KeyboardController(DynamicPath):
    def process_event(self, event):
        if isinstance(event, KeyboardEvent):
            key = event.key_code
            if key == Screen.KEY_UP:
                self._y -= 1
                self._y = max(self._y, 2)
            elif key == Screen.KEY_DOWN:
                self._y += 1
                self._y = min(self._y, self._screen.height-2)
            elif key == Screen.KEY_LEFT:
                self._x -= 1
                self._x = max(self._x, 3)
            elif key == Screen.KEY_RIGHT:
                self._x += 1
                self._x = min(self._x, self._screen.width-3)
            else:
                return event
        else:
            return event
"""

def demo(screen):

    scenes = []
    effects = [
        Print(screen,
              ColourImageFile(screen, "tenor.gif", screen.height - 2,
                              uni=screen.unicode_aware,
                              dither=screen.unicode_aware),
              0,
              stop_frame=200),
        Print(screen,
              FigletText("WASP",
                         font='epic' if screen.width > 80 else 'banner'),
              screen.height // 2 - 3,
              colour=7, bg=7 if screen.unicode_aware else 0),
        Print(screen,
              SpeechBubble("press <Space> to continue "),
              screen.height - 5,
              speed=1, transparent=False)
    ]
    scenes.append(Scene(effects))
    effects = [
        Print(screen, ImageFile("love.gif", screen.height - 2, colours=screen.colours),
              0,
              stop_frame=100),
    ]
    scenes.append(Scene(effects))

    effects = [
        Print(screen, ImageFile("sad_to_happy.gif", screen.height - 2, colours=screen.colours),
              0,
              stop_frame=100),
    ]
    scenes.append(Scene(effects))

    effects = [
        Print(screen, ImageFile("sad.jpg", screen.height - 2, colours=screen.colours),
              0,
              stop_frame=100),
    ]
    scenes.append(Scene(effects))

    effects = [
        Print(screen, ImageFile("neutral.jpg", screen.height - 2, colours=screen.colours),
              0,
              stop_frame=100),
    ]
    scenes.append(Scene(effects))

    effects = [
        Print(screen, ImageFile("smile.jpg", screen.height - 2, colours=screen.colours),
              0,
              stop_frame=100),
    ]
    scenes.append(Scene(effects))

    effects = [
        Print(screen, ImageFile("smiling.jpg", screen.height - 2, colours=screen.colours),
              0,
              stop_frame=100),
    ]
    scenes.append(Scene(effects))

    effects = [
        Print(screen, ImageFile("broken_heart.jpg", screen.height - 2, colours=screen.colours),
              0,
              stop_frame=100),
    ]
    scenes.append(Scene(effects))

    effects = [
        Print(screen, ImageFile("heart.jpg", screen.height - 2, colours=screen.colours),
              0,
              stop_frame=100),
    ]
    scenes.append(Scene(effects))

    effects = [
        Print(screen, ColourImageFile(screen, "poop.jpg", screen.height - 2,
                                      uni=screen.unicode_aware, dither=screen.unicode_aware),
              0,
              stop_frame=100),
        Print(screen,
              SpeechBubble("press <X> to exit "),
              screen.height - 5,
              speed=1, transparent=False)
    ]
    scenes.append(Scene(effects))

    screen.play(scenes, stop_on_resize=True)


if __name__ == "__main__":
    while True:
        try:
            Screen.wrapper(demo)
            sys.exit(0)
        except ResizeScreenError:
            pass

"""  effects = [
        Print(screen,
              ColourImageFile(screen, "sad.jpg", screen.height,
                              uni=screen.unicode_aware),
              screen.height,
              speed=1,
              stop_frame=(40+screen.height)*3),
        Scroll(screen, 3)
    ]
    scenes.append(Scene(effects))
    effects = [
        BannerText(screen,
                   ColourImageFile(screen, "sad.jpg", screen.height-2,
                                   uni=screen.unicode_aware, dither=screen.unicode_aware),
                   0, 0),
    ]
    scenes.append(Scene(effects))

"""

demo(screen)
