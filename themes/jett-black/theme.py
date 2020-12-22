import reflux

from reflux.values import COLORS

t = reflux.Theme({
    "name": "Jett-Black",
    "author": "IreTheKID",
    "description": "Lights out >:)",
    "default": "dark"
})

for n, v in COLORS["dark"].items():
    t.set_color(n, "black")

t.build("themes/jett-black/theme.min.js")
