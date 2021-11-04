import os
import pathlib

path = pathlib.Path(__file__).parent.resolve()


class Resources(object):
    def __init__(self):
        self.categories = ["root", "light", "dark"]
        self.headers = {
            "root": ".replit-ui-theme-root, :root",
            "tokens": ".replit-ui-theme-root.light, .replit-ui-theme-root.dark",
        }

        for file in os.scandir(f"{path}/resources/variables"):
            name = file.name.split(".")[0]

            if file.is_file() and file.name.endswith(".txt"):
                contents = open(file).read()
                jar = self._create_var_jar(contents)

                jar["_keys"] = list(jar.keys())

                self.__setattr__(name, jar)
        
        self.engine = "javascript:" + open(f"{path}/engine/reflux.min.js").read()

    def _create_var_jar(self, contents: str):
        jar = {}

        for line in contents.split(";\n"):
            k, v = line.split(":")
            jar[k] = v[1:]

        return jar


shelf = Resources()
