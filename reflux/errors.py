class Error(Exception):
    pass


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