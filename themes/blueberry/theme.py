import reflux

t = reflux.Theme({
    "name": "Blueberry",
    "author": "IreTheKID",
    "description": "Make your Repl IDE a blueberry color scheme!",
    "default": "dark"
})

t.set_colors({
    
})

open("themes/blueberry/theme.min.js", "w+").write(t.build())
