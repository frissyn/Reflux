from .values import JS
from .values import CSS
from .values import COLORS
from .values import DEFAULT

def update(stale, new):
    for n, v in new.items():
        stale[n] = v
    
    return stale


class Theme(object):
    def __init__(self, obj):
        self.obj = update(DEFAULT, obj)
        self.obj["colors"] = COLORS[obj["default"]]
    
    def set_color(self, name: str, value: str):
        target = self.obj["colors"][name]

        target = value

        return target

    def set_colors(self, obj: dict):
        self.obj["colors"] = update(self.obj["colors"], obj)
    
    def get_color(self, name: str):
        try:
            return self.obj["colors"][name]
        except ValueError:
            return None
    
    def build(self, path, mode="w+"):
        js = JS
        css = ""
        file = open(path, mode)

        for n, v in self.obj["colors"].items():
            css += f"--color-{n}: {v} !important;"
        
        for n, v in self.obj.items():
            if not isinstance(v, dict):
                js = js.replace(f"!{n}!", str(v))
        
        css = CSS.replace("!css!", css)

        js = (
            js
            .replace("!css!", css)
            .replace("\n", "")
            .replace("\t", "")
            .replace("    ", "")
            .replace(" = ", "=")
        )

        file.write(js)
        file.close()

        return True
