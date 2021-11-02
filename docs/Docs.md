# Reflux: Python Documentation

### `reflux.Theme`

Base class for creating, parsing, and uploading Reflux themes.

|Function|Example|Description|
|:-------|:-----:|:----------|
|`__init__(path)`|`Theme("theme.yaml")`|Parses and creates a theme.|
|`theme.upload(publish_key)`|`theme.upload("gRVxeIYoGGGfHxbM-lKJQw")`|Uploads the theme to Reflux with a user's publish key.|
|`theme.referral`|`theme.referral()`|Returns the theme's referral code. Raises an error if theme has not been uploaded.|
|`theme.to_stylesheet(file=None)`|`theme.to_stylesheet(file="theme.css")`|Generates a CSS stylesheet from the theme and returns the text. Saves to filename if provided.|

### `reflux.errors`

Errors that might be raised when using Reflux.

|Error|Description|
|:----|:----------|
|`RefluxAPIError`|Raised when an error occurs when interacting with the API.|
|`NotUploadedError`|Raised when calling `theme.referral()` without uploding the theme.|
|`MissingFieldError`|Raised when a field is missing from the theme file.|
|`MissingCategoryError`|Raised when a category is missing from the theme file.|