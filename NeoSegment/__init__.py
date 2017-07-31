from bibliopixel.layout.strip import Strip
from bibliopixel.animation import BaseAnimation
from bibliopixel import data_maker
from bibliopixel import colors

CHAR_OFFSET = 32

_characters = [
    0b00000000,
    0b00000000,
    0b01010000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b01000000,
    0b00110011,
    0b01100110,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00001000,
    0b00000000,
    0b00000000,
    0b01110111,
    0b01000100,
    0b01101011,
    0b01101110,
    0b01011100,
    0b00111110,
    0b00111111,
    0b01100100,
    0b01111111,
    0b01111110,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b01111101,
    0b01111111,
    0b00110011,
    0b01110111,
    0b00111011,
    0b00111001,
    0b00110111,
    0b01011101,
    0b01000100,
    0b01000111,
    0b01011101,
    0b00010011,
    0b00101101,
    0b00001101,
    0b01110111,
    0b01111001,
    0b01111100,
    0b01111101,
    0b00111110,
    0b00110001,
    0b01010111,
    0b01011001,
    0b01011111,
    0b01001001,
    0b01011110,
    0b01101011,
    0b00110011,
    0b00000000,
    0b01100110,
    0b00000000,
    0b00000010,
    0b00010000,
    0b01101111,
    0b00011111,
    0b00001011,
    0b01001111,
    0b01111011,
    0b00111001,
    0b01111110,
    0b00011101,
    0b00000100,
    0b01000110,
    0b00011101,
    0b00010001,
    0b00101101,
    0b00001101,
    0b00001111,
    0b01111001,
    0b01111100,
    0b00001001,
    0b00111110,
    0b00011011,
    0b00000111,
    0b01011000,
    0b01011010,
    0b01001001,
    0b01011100,
    0b01101011
]
CHAR_COUNT = len(_characters)


class NeoSegment(Strip):
    def __init__(self, drivers, threadedUpdate=False,
                 brightness=255, **kwargs):
        super().__init__(drivers, threadedUpdate, brightness,
                         maker=kwargs.get('maker', data_maker.MAKER))

        if self.numLEDs % 7 != 0:
            raise ValueError('Each NeoSegment has 7 pixels.'
                             ' Total size should be multiple of 7.')

        self.numDigits = self.numLEDs // 7

    def set(self, pixel, color):
        self._set_base(pixel, color)

    def set_char(self, c, color, off_color=colors.Off, index=0):
        index = index * 7
        c = ord(c)
        if not isinstance(color, list):
            color = [color] * 7

        if c - CHAR_OFFSET < CHAR_COUNT:
            c_val = _characters[c - CHAR_OFFSET]
            for i in range(7):
                if c_val & (1 << i):
                    self.set(index + i, color[i])
                else:
                    self.set(index + i, off_color)

    def set_text(self, text, color, off_color=colors.Off, index=0):
        if not isinstance(color, list):
            color = [color] * len(text)
        for i, c in enumerate(text):
            self.set_char(c, color[i], off_color, index)
            index += 1


class BaseNeoSegmentAnim(BaseAnimation):
    def __init__(self, layout):
        super().__init__(layout)
        self.numDigits = self.layout.numDigits
