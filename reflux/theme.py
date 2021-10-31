import yaml

from .resources import shelf

from .errors import MissingFieldError
from .errors import MissingCategoryError

class Theme(object):
    def __init__(self, path):
        with open(path, "r") as stream:
            data = yaml.safe_load(stream)
        
        self._raise_for_errors(data)

        self.name        = data["Meta"]["name"]
        self.description = data["Meta"]["description"]

        self.styles = {
            "root": shelf.root,
            "light": shelf.light,
            "dark": shelf.dark
        }

        for c in shelf.categories:
            category = data.get(c)

            if category:
                self.styles[c].update(data[c])

    def _raise_for_missing_errors(d):
        if not d.get("Meta"):
            raise MissingCategoryError("Theme", "Meta")
        
        for c in ["name", "description"]:
            if not d["Meta"].get(c):
                raise MissingFieldError("Meta", c)
        
        return