import reflux

t = reflux.Theme({
    "name": "Blueberry",
    "author": "frissyn",
    "description": "Make your Repl IDE a blueberry color scheme!",
    "default": "dark"
})

t.set_colors({
    "border": "#00008b",

    "background-1": "#6495ed",
    "background-2": "#76a1ef",
    "background-3": "#87adf1",

    "primary-1": "#00008b",
    "primary-2": "#00009f",
    "primary-3": "#0000b2",
    "primary-4": "#0000c6",

    "positive-1": "#000077",
    "positive-2": "#00008b",
    "positive-3": "#00009f",
    "positive-4": "#0000b2",

    "foreground-1": "#590059",
    "foreground-2": "#450045",
    "foreground-3": "#320032",
    "foreground-4": "#1e001e",

    "positive-transparent-1": "rgba(0, 0, 139, 0.48)",
    "positive-transparent-2": "rgba(0, 0, 139, 0.24)",
    "positive-transparent-3": "rgba(0, 0, 139, 0.12)",
})

t.build("themes/blueberry/theme.min.js")
