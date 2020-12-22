# Source

#### [`reflux/themes.py`](https://github.com/IreTheKID/Reflux/blob/master/reflux/theme.py)

# Quickstart
```python
import reflux

theme = reflux.Theme({
    "name": "New Theme",
    "author": "Myself",
    "description": None,
    "default": "light"
})
```


# Functions

| \_\_init\_\_(*obj*)| Initialize the `Theme` object.                                    |
|:-------------------|:------------------------------------------------------------------|

| Parameters                                                                             |
|:------------|:----------------|:-------------------------------------------------------|
| name        | `str` or `None` | Name of the theme. Defaults to `None`.                 |
| author      | `str` or `None` | Author of the theme. Defaults to `None`.               |
| description | `str` or `None` | Description of the theme. Defaults to `None`.          |
| default     | `str`           | Default color values for theme. Defaults to `"light"`. |

**Note**: These are not named parameters. They are key-value pairs in the passed `obj`.

---

| set_color(*name*, *value*)| Set a color to a given value.                              |
|:-------------------|:------------------------------------------------------------------|

| Parameters                                                                             |
|:------------|:----------------|:-------------------------------------------------------|
| name        | `str`           | Name of the color value to be set.                     |
| value       | `str`           | Any CSS3 compatible color value.                       |

---

| set_colors(*obj*)  | Sets multiple colors to the given values in a `dict`.             |
|:-------------------|:------------------------------------------------------------------|

| Parameters                                                                             |
|:------------|:----------------|:-------------------------------------------------------|
| obj         | `dict`          | keys are color names, values are color values.         |

---

| get_color(*name*)| Get the current value of a given color name. `None` if not found.   |
|:-------------------|:------------------------------------------------------------------|

| Parameters                                                                             |
|:------------|:----------------|:-------------------------------------------------------|
| name        | `str`           | Name of the color to get.                              |

---

| build(*path*, *mode*)| Builds a JS Reflux theme with the current colors to the given file. |
|:-------------------|:----------------------------------------------------------------------|

| Parameters                                                                             |
|:------------|:----------------|:-------------------------------------------------------|
| path        | `str`           | Path to the target file. Should be a valid directory.  |
| mode        | `str`           | [Mode character](https://docs.python.org/3/library/functions.html#open) to open the file with.|
