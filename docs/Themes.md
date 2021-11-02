# Using Theme Files

Reflux uses `YAML` files to create and generate themes on Replit. The file contains metadata for the theme, and of course, all the CSS tokens. These files can be saved with either a `.yml` or `.yaml` extension, just make sure to name it properly when loading it in Reflux.

## Specification


**Category:** Meta, *required*

**Fields:**
+ name, *required* - name of the theme, if you already have a theme with this name, uploading it will edit it
+ description, *required* - description of the theme, spice it up if you want people to use your theme!

**Example:**
```yaml
Meta:
    name: Solarized Dark
    description: The classic dark theme for machines and people, now on Replit!
```

-----

**Category:** Styles, *required*

**Subcategories:**
+ root, *optional* - define CSS tokens for the `:root`, you rarely need to change these
+ tokens, *optinal* - define CSS tokens for both light and dark themes

**Example:**
```yaml
Styles:
    root:
        --border-radius-1: 1px
        --border-radius-2: 2px
    tokens:
        --background-root: "#0e1525"
        --background-default: "#1c2333"
```

## References

You can find a complete index of all the CSS tokens [here]().

Here's a complete example of a finished theme for reference:

```yaml
Meta:
    name: Solarized Dark
    description: The classic dark theme for machines and people, now on Replit!

Styles:
    root:
        # Nothing to change here
    tokens:
        # Background Tokens
        # Assigned from Base03 to Base00
        --background-root: "#001b22"
        --background-default: "#002b36"
        --background-higher: "#073642"
        --background-highest: "#586e75"
        --background-overlay: "#0e1525a0"

        # Forground Tokens
        # Assigned from Base2 and Base3
        --foreground-default: "#e8e0c7"
        --foreground-dimmer: "#eee8d5"
        --foreground-dimmest: "#f4f0e3"

        # Primary Accent Tokens
        # Assigned from Blue Accents
        --accent-primary-strongest: "#1a5f90"
        --accent-primary-stronger: "#2075b1"
        --accent-primary-default: "#268bd2"
        --accent-primary-dimmer: "#429ddd"
        --accent-primary-dimmest: "#64aee3"

        # Red Accent Tokens
        # Assigned from Red Accents
        --accent-red-dimmest: "#850101"
        --accent-red-dimmer: "#ac0102"
        --accent-red-default: "#d30102"
        --accent-red-stronger: "#fa0102"
        --accent-red-strongest: "#fe2426"
```