import reflux

t = reflux.Theme({
    "name": "Cactus",
    "author": "frissyn",
    "description": "Coding Cactus' trademark theme!",
    "default": "dark"
})

t.set_colors({
    "border": "#32cd32",

    "control-1": "#0c2f0c",
    "control-2": "#103f10",
    "control-3": "#144f14",

    "foreground-1": "#cccccc",
    "foreground-2": "#c2c2c2",
    "foreground-3": "#b8b8b8",
    "foreground-4": "#adadad",

    "primary-1": "#eb8100",
    "primary-2": "#d87600",
    "primary-3": "#c46c00",
    "primary-4": "#b16100",

    "background-1": "#0f3f0f",
    "background-2": "#0c2f0c",
    "background-3": "#082008",
    "background-4": "#041004"
})

t.build("themes/cactus/theme.min.js", "w+")
