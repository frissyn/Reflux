import yaml

from .resources import shelf

from .errors import MissingFieldError
from .errors import MissingCategoryError

class Theme(object):
    def __init__(self, path):
        with open(path, "r") as stream:
            data = yaml.safe_load(stream)
        
        self._raise_for_errors(data)

        self.name = data["Meta"]["name"]
        self.description = data["Meta"]["description"]

        self.styles = {
            "root": shelf.root,
            "light": shelf.light,
            "dark": shelf.dark
        }

        for c in shelf.categories:
            category = data["Styles"].get(c)

            if category:
                self.styles[c].update(data["Styles"][c])

    def _raise_for_errors(self, d):
        for t in ["Meta", "Styles"]:
            if not d.get(t):
                raise MissingCategoryError("Theme", t)

        for f in ["name", "description"]:
            if not d["Meta"].get(f):
                raise MissingFieldError("Meta", f)
        
        return
    
    def to_stylesheet(self, file=None):
        text = ""

        for key in self.styles.keys():
            text += shelf.headers[key] + " {"

            for k, v in self.styles[key].items():
                if not k.startswith("_") and k != "":
                    text += f"{k}: {v} !important;"
            
            text += "}"
        
        if file:
            with open(file, "w+") as f:
                f.write(text)
        
        return text