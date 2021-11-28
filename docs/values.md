# Source

#### [`reflux/themes.py`](https://github.com/IreTheKID/Reflux/blob/master/reflux/values.py)

# Quickstart
```python
from reflux.values import COLORS

print("Light Theme Colors =", COLORS["light"])

print("Dark Theme Colors =", COLORS["dark"])
```

# Details

Reflux builds JavaScript Bookmarklets that inject CSS with your theme's color values. It overwrites Repl.it's default CSS by rewriting the classes that the IDE uses for colors. You can find a collection of all Repl.it's CSS styles [right here](https://github.com/IreTheKID/Repl.it-CSS-Index).

# Index

Here are all the default IDE colors for both light and dark modes. You can change them with `theme.set_color` or `theme.set_colors`.

```ini
[LIGHT MODE COLORS]
background-1             = "#ffffff"
background-2             = "#f6f6f6"
background-3             = "#eeeeee"
control-1                = "#e0e0e0"
control-2                = "#e9e9e9"
control-3                = "#f3f3f3"
border                   = "#e0e0e0"
foreground-1             = "#363636"
foreground-2             = "#6f6f6f"
foreground-3             = "#949494"
foreground-4             = "#b7b7b7"
foreground-transparent-1 = "rgba(255 255 255 0.48)"
foreground-transparent-2 = "rgba(255 255 255 0.24)"
foreground-transparent-3 = "rgba(255 255 255 0.12)"
primary-1                = "#3485e4"
primary-2                = "#337ad1"
primary-3                = "#3272c2"
primary-4                = "#316ab4"
primary-transparent-1    = "rgba(52 133 228 0.48)"
primary-transparent-2    = "rgba(52 133 228 0.24)"
primary-transparent-3    = "rgba(52 133 228 0.12)"
negative-1               = "#ff491c"
negative-2               = "#e9441b"
negative-3               = "#d8411b"
negative-4               = "#c93d1a"
negative-transparent-1   = "rgba(255 73 28 0.48)"
negative-transparent-2   = "rgba(255 73 28 0.24)"
negative-transparent-3   = "rgba(255 73 28 0.12)"
warning-1                = "#eb6404"
warning-2                = "#d65c08"
warning-3                = "#c7560b"
warning-4                = "#b8510d"
warning-transparent-1    = "rgba(242 103 2 0.48)"
warning-transparent-2    = "rgba(242 103 2 0.24)"
warning-transparent-3    = "rgba(242 103 2 0.12)"
positive-1               = "#21a243"
positive-2               = "#21953e"
positive-3               = "#228a3a"
positive-4               = "#228037"
positive-transparent-1   = "rgba(24 204 81 0.48)"
positive-transparent-2   = "rgba(24 204 81 0.24)"
positive-transparent-3   = "rgba(24 204 81 0.12)"

[DARK MODE COLROS]
background-1             = "#1d2333",
background-2             = "#171d2d",
background-3             = "#0e1525",
control-1                = "#313646",
control-2                = "#2b3140",
control-3                = "#262b3b",
border-1                 = "#313646",
foreground-1             = "#e1e2e4",
foreground-2             = "#90939c",
foreground-3             = "#696d78",
foreground-4             = "#4e525f",
foreground-transparent-1 = "rgba(14, 21, 37, 0.48)",
foreground-transparent-2 = "rgba(14, 21, 37, 0.24)",
foreground-transparent-3 = "rgba(14, 21, 37, 0.12)",
primary-1                = "#3485e4",
primary-2                = "#337bd2",
primary-3                = "#3273c4",
primary-4                = "#316cb8",
primary-transparent-1    = "rgba(52, 133, 228, 0.48)",
primary-transparent-2    = "rgba(52, 133, 228, 0.24)",
primary-transparent-3    = "rgba(52, 133, 228, 0.12)",
negative-1               = "#ff491c",
negative-2               = "#eb451b",
negative-3               = "#db411b",
negative-4               = "#cd3e1a",
negative-transparent-1   = "rgba(255, 73, 28, 0.48)",
negative-transparent-2   = "rgba(255, 73, 28, 0.24)",
negative-transparent-3   = "rgba(255, 73, 28, 0.12)",
warning-1                = "#f26702",
warning-2                = "#de5f07",
warning-3                = "#ce590a",
warning-4                = "#c0540c",
warning-transparent-1    = "rgba(242, 103, 2, 0.48)",
warning-transparent-2    = "rgba(242, 103, 2, 0.24)",
warning-transparent-3    = "rgba(242, 103, 2, 0.12)",
positive-1               = "#20ab46",
positive-2               = "#219d41",
positive-3               = "#22923d",
positive-4               = "#22883a",
positive-transparent-1   = "rgba(24, 204, 81, 0.48)",
positive-transparent-2   = "rgba(24, 204, 81, 0.24)",
positive-transparent-3   = "rgba(24, 204, 81, 0.12)"
```
