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
        self.styles = {"root": shelf.root, "tokens": shelf.dark}

        if data["Styles"].get("root"):
            self.styles["root"].update(data["Styles"]["root"])
        
        if data["Styles"].get("tokens"):
            self.styles["tokens"].update(data["Styles"]["tokens"])

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

        for header in ["root", "tokens"]:
            if self.styles.get(header):
                text += shelf.headers[header] + "{"

                for token, value in self.styles[header].items():
                    if not token.startswith("_") and token != "":
                        text += f"{token}: {value} !important;"
                
                text += "}"
        
        text = text.replace(" !important;}", "}")
        
        if file:
            with open(file, "w+") as f:
                f.write(text)
        
        return text