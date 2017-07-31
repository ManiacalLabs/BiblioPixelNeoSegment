from NeoSegment import BaseNeoSegmentAnim
from bibliopixel import colors
import time


class RGBClock(BaseNeoSegmentAnim):
    """Fill the dots progressively along the strip."""

    def __init__(self, layout):
        super().__init__(layout)

    def step(self, amt=1):
        t = time.localtime()
        self.layout.all_off()
        c = colors.hue2rgb((t.tm_hour - 12) * (256 // 12))
        self.layout.set_text(str(t.tm_hour - 12).zfill(2), c, index=0)

        c = colors.hue2rgb(t.tm_min * (256 // 60))
        self.layout.set_text(str(t.tm_min).zfill(2), c, index=2)

        c = colors.hue2rgb(t.tm_sec * (256 // 60))
        self.layout.set_text(str(t.tm_sec).zfill(2), c, index=4)

        self._step = 0


class ScrollText(BaseNeoSegmentAnim):
    """Fill the dots progressively along the strip."""

    def __init__(self, layout, msg, colors):
        super().__init__(layout)
        self.msg = (' ' * self.numDigits) + msg
        self.colors = colors

    def step(self, amt=1):
        self.layout.all_off()
        c = self.colors[self._step % len(self.colors)]
        self.layout.set_text(self.msg[self._step:self._step + self.numDigits], c)

        self._step += 1
        if self._step >= len(self.msg):
            self._step = 0
            self.completed = True
