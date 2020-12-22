import reflux

t = reflux.Theme({
    "name": "Candyland",
    "author": "IreTheKID",
    "description": "Turn your Repl IDE into a candy wonderland!",
    "default": "light"
})

t.set_colors({
    "border": "#32cd32",

    "background-1": "#ffc0cb",
    "background-2": "#ffacbb",
    "background-3": "#ff99ab",

    "primary-1": "#ff1493",
    "primary-2": "#ff289c",
    "primary-3": "#ff3ba5",
    "primary-4": "#ff4fae",

    "positive-1": "#ff1493",
    "positive-2": "#ff289c",
    "positive-3": "#ff3ba5",
    "positive-4": "#ff4fae",

    "foreground-1": "#006400",
    "foreground-2": "#005000",
    "foreground-3": "#003d00",
    "foreground-4": "#002900",

    "positive-transparent-1": "rgba(255, 20, 147, 0.48)",
    "positive-transparent-2": "rgba(255, 20, 147, 0.24)",
    "positive-transparent-3": "rgba(255, 20, 147, 0.12)",
})

t.build("themes/candyland/theme.min.js")
