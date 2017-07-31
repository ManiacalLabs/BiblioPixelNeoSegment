Adds BiblioPixel support for the NeoSegment: https://www.crowdsupply.com/maksmakes/neosegment

Installation: `pip install BiblioPixelNeoSegment`

### Usage

Import the NeoSegment `layout` which is used like other BiblioPixel [layouts](https://github.com/ManiacalLabs/BiblioPixel/wiki/Layout).

`from NeoSegment import NeoSegment`

If creating an animation for NeoSegment you can use `BaseNeoSegmentAnim`:

```
from NeoSegment import BaseNeoSegmentAnim

class NeoSegAnimation(BaseNeoSegmentAnim):
    def __init__(self, layout):
        super().__init__(layout)

    def step(self, amt=1):
        # your animation code here

```

Two demo animations are included: `from NeoSegment.demo_anims import RGBClock, ScrollText`

These are used as examples in [demo.py](https://github.com/ManiacalLabs/BiblioPixelNeoSegment/blob/master/demo.py)


### NeoSegment class

#### `__init__(...)`

Constructor has all of the same options as the [`strip`](https://github.com/ManiacalLabs/BiblioPixel/wiki/Strip) layout.

#### `set(pixel, color)`

For setting specific individual segments of each digit. Each digit has 7 segments which are arranged as such:

```
  5
4   6
  3
0   2
  1
```

`pixel` is the index of the segment you want to set and `color` is a standard BiblioPixel color tuple `(r, g, b)`. You can of course use the `bibliopixel.colors` module.

For digits after the first the index of each segment is `seg_index + (7 * digit_index)`

#### `set_char(c, color, off_color=colors.Off, index=0)`

Sets a specific digit to the given character `c`. This is used by `set_text`.

- `c`: Single character to set to given digit. Alphanumeric and and `![]- ` are allowed.
- `color`: A single BiblioPixel color tuple or list of colors. If a list, 7 must be provided and each will be used for the same segment index. In this way each segment can be a different color.
- `off_color`: Color tuple to use for segments that are unset in the digit. Defaults to Off.
- `index`: Index of digit in chain to set. Indices are left to right on the NeoSegment chain.

#### `set_text(text, color, off_color=colors.Off, index=0)`

Writes a string to the display.

- `text`: String to write to display. Invalid characters will result in a blank digit.
- `color`: A single BiblioPixel color tuple or list of colors or list of lists of colors. If a list, each digit will be the color at the same index in the list. Provide a list of lists to specify the color of each individual segment of each digit.
- `off_color`: Same as `set_text`
- `index`: Index of digit to start string.
