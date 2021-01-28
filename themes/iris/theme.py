import reflux

t = reflux.Theme({
    "name": "Iris",
    "author": "frissyn",
    "description": "A dark mix of purple and yellow.",
    "default": "dark"
})

t.set_colors({
    "border": "#7b16f0",

    "control-1": "#461c6a",
    "control-2": "#3c185b",
    "control-3": "#32144b",

    "primary-1": "#b98500",
    "primary-2": "#a57700",
    "primary-3": "#916900",
    "primary-4": "#7e5b00",

    "background-1": "#280551",
    "background-2": "#1f043e",
    "background-3": "#16032c",
    "background-4": "#0d0219"
})

t.build("themes/iris/theme.min.js", "w+")