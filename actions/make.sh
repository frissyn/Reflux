#!/bin/bash

echo -n "Theme Name >> "; read name

if python "themes/$name/theme.py"; then
    printf "\n\Theme '$name' made successfully.\n"
else
    printf "\n\nAn error occured building `$name` theme.\n"
    exit 1
fi