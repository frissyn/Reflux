class Error(Exception):
    pass

class RefluxAPIError(Error):
    def __init__(self, code, context):
        self.code = code
        self.error = ""
        self.context = context.body

        if self.code == 400:
            self.error = "Theme could not be formatted correctly."
        elif self.code == 401:
            self.error = "Provided publish_key is invalid or expired."
        elif self.code == 500:
            self.error = "The API encounted an internal error, please try again later."
    
    def __str__(self):
        return f"{self.error}\nRaw response:{self.context}"

class NotUploadedError(Error):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return (
            f"Theme '{self.name}' has no upload data." +
            " Please upload the theme before getting a referral code."
        )


class MissingFieldError(Error):
    def __init__(self, name, field):
        self.name = name
        self.field = field
    
    def __str__(self):
        return f"{self.name} is missing required field: '{self.field}'"


class MissingCategoryError(Error):
    def __init__(self, name, cat):
        self.name = name
        self.cat = cat
    
    def __str__(self):
        return f"{self.name} is missing required category: '{self.cat}'"