# Reflux: A Repl.it IDE Theming Tool [![Run on Repl.it](https://repl.it/badge/github/frissyn/Reflux)](https://repl.it/github/frissyn/Reflux)

Reflux is a tool to create and modify the default styles that apply to your IDE on [Repl.it](https://repl.it/). Using Python, you can create themes, set colors, and generate easy-to-use JavaScript Bookmarlets for use in any Repl. Designed so that those who are unfamiliar with Python can still create themes!

**Recent Update: `v0.2.0`:**
Reflux themes will now work outside of the IDE more consistently. Rebuild your themes to reflect these changes!

# Overview

### Installation

|Manager          |Command                                       |
|:----------------|:---------------------------------------------|
|**pip**          |`pip install reflux`                          |
|**poetry**       |`python -m poetry add reflux`                 |
|**Repl.it**      |Search `reflux` in the package tab and add it.|

### Quickstart

```python
import reflux

t = reflux.Theme({
    "name": "New Theme",
    "author": "Your Username",
    "description": "A simple theme to get started with!",
    "default": "light"
})

t.set_color("primary-1", "whitesmoke")

t.set_colors({
    "primary-2": "rbga(255, 255, 255, 0.48)",
    "primary-3": "hsl(0, 100%, 50%)"
})

t.build("mytheme.min.js")
```

Then copy the resulting JS code into a bookmarklet in your broswer, and run it in your Repl! (Running it again will prompt you for an option to turn it off). Try it out with one of the premade themes [here](https://github.com/frissyn/Reflux/tree/master/themes)! Images of these themes are in their respective folders.

You can find a complete tutorial on Reflux themes [here](https://repl.it/talk/x/x/118029)!

### Examples

![iris](https://storage.googleapis.com/replit/images/1611845083584_d6428aecacbdab9478764c700f76a665.png)
![candyland](https://storage.googleapis.com/replit/images/1611845281908_6869f49b3d2a3722fbb766c96aeae0cc.png)
![blueberry](https://storage.googleapis.com/replit/images/1611845384713_7d7bc415e3615439edbcd1fce6576054.png)
