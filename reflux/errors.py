class Error(Exception):
    pass


class MissingFieldError(Error):
    def __init__(self, field, subject):
        self.field   = field
        self.subject = subject
    
    def __str__(self):
        return f"{self.subject} is missing required field: '{self.field}'"


class MissingCategoryError(Error):
    def __init__(self, cat, subject):
        self.cat     = cat
        self.subject = subject
    
    def __str__(self):
        return f"{self.subject} is missing required category: '{self.cat}'"