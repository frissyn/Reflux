# import os
import pathlib
# import importlib

path = pathlib.Path(__file__).parent


class Resources(object):
    def __init__(self):
        self.categories = ["root", "light", "dark"]
        self.headers = {
            "root": ".replit-ui-theme-root, :root",
            "tokens": ".replit-ui-theme-root.light, .replit-ui-theme-root.dark",
        }

        self.engine = "javascript:"
        self.engine += path.joinpath("engine/reflux.min.js").read_text()
        
        for c in self.categories:
            content = path.joinpath(f"variables/{c}.txt")

            jar = self._create_var_jar(content.read_text())
            jar["_keys"] = list(jar.keys())

            self.__setattr__(c, jar)

    def _create_var_jar(self, contents: str):
        jar = {}

        for line in contents.split(";\n"):
            k, v = line.split(":")
            jar[k] = v[1:]

        return jar


shelf = Resources()
