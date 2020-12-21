# Reflux: A Repl.it IDE Theming Tool

Reflux is a tool to create and modify the default styles that apply to your IDE on [Repl.it](https://repl.it/). Using Python, you can create themes, set colors, and generate easy-to-use JavaScript Bookmarlets for use in any Repl. (Currently in Beta!)

## Quickstart

```python
import reflux

t = reflux.Theme({
    "name": "New Theme",
    "author": "Your Username",
    "description": "A simple theme to get started with!",
    "default": "light"
})

t.set_color("primary-1", "whitesmoke")

open("theme.min.js", "w+").write(t.build())
```

Then copy the resulting JS code into a bookmarklet in your broswer, and run it in your Repl! (Running it again, will prompt you for an option to turn it off). Try it out with the [Candyland](https://github.com/IreTheKID/Reflux/tree/master/themes/candyland) theme!

![image](https://storage.googleapis.com/replit/images/1608561552325_de2b5793e1c4702278c2f4801e9be7e5.png)