import os
import pathlib

path = pathlib.Path(__file__).parent.resolve()

class Resources(object):
    def __init__(self):
        for file in os.scandir(f"{path}/variables"):
            name = file.name.split(".")[0]

            if file.is_file() and file.name.endswith(".txt"):
                contents = open(file).read()
                jar = self.create_var_jar(contents)

                jar["_keys"] = list(jar.keys())

                self.__setattr__(name, jar)

    def create_var_jar(self, contents: str):
        jar = {}

        for line in contents.split(";\n"):
            k, v = line.split(":")
            
            if k[:2] == "--":
                k = k.replace("--", "")

            jar[k] = v[1:]

        return jar

resources = Resources()