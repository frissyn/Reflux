import yaml
import pathlib
import requests

from reflux.resources import shelf

from reflux.errors import RefluxAPIError
from reflux.errors import NotUploadedError
from reflux.errors import MissingFieldError
from reflux.errors import MissingCategoryError

API = "https://api.reflux.repl.co"
PATH = pathlib.Path(__file__).parent.resolve()


def make_engine(code: str, file=None):
    engine = shelf.theme_engine.replace("{{ referral }}", code)

    if file:
        with open(file, "w+") as stream:
            stream.write(engine)

    return engine


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

        if "Advanced" in data.keys():
            if "monaco" in data["Advanced"]:
                self.monaco = data["Advanced"]["monaco"]
            if "xterm" in data["Advanced"]:
                self.xterm = data["Advanced"]["xterm"]

    def _raise_for_errors(self, d):
        for t in ["Meta", "Styles"]:
            if not d.get(t):
                raise MissingCategoryError("Theme", t)

        for f in ["name", "description"]:
            if not d["Meta"].get(f):
                raise MissingFieldError("Meta", f)

        return

    def _raise_for_responses(self, r):
        if r.status_code >= 400:
            raise RefluxAPIError(r.status_code, r)
        else:
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

    def upload(self, publish_key):
        r = requests.post(
            f"{API}/theme/upload",
            json={
                "name": self.name,
                "description": self.description,
                "stylesheet": self.to_stylesheet(),
                "monaco": self.monaco,
                "xterm": self.xterm,
                "publish_key": publish_key,
            },
        )

        self._raise_for_responses(r)
        self.data = r.json()

        return self.data

    def referral(self):
        try:
            return self.data["referral"]
        except:
            raise NotUploadedError(self.name)

    def engine(self, file=None):
        return make_engine(self.referral(), file)
