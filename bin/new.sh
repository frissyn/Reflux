#!/bin/bash

echo -n "Theme Name >> "; read name

if [-f "themes/$name"]; then
    echo "Theme directory for `$name` already exists."
else
    mkdir "themes/$name"
    touch "themes/$name/theme.min.js"
    touch "themes/$name/theme.py"
    echo "Theme directory for `$name` successfully created."
fi
