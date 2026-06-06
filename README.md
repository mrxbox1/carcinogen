# carcinogen

## Usage
### In the MD file
These\
`@[INSERT TITLE HERE]`\
`@[INSERT CSS FILE HERE]`\
as the first two lines in the MD file will override the title of the HTML page and the CSS file that is embedded.

### In the command line
`python3 carcinogen.py [MD_FILE] [HTML_OUTPUT_FILE] [CSS_FILE]`\
_(These aren't the actual names of the parameters.)_\
**Important:** the code is kind of messy right now, so if you're going to embed a CSS file within the first two lines of the MD file, the `[CSS_FILE]` argument will do nothing.

### Recommendation
This project is meant to be used as a supplementary Python script, not a Python package. Regardless, it is stored in this repo as a Python package because I have no idea how to turn it into a Python package correctly, and so, it is stuck here as a Python package. Just do me a favor and copy the script into your website's repository instead of using it as a Python package, okay?

## What is this?
'Carcinogen' is a little pet project that I'm using to generate HTML pages from MD files. Yes, projects like this exist
already, but I figured I'd make my own, objectively worse one, in Python, my favorite (INTERPRETED) language.

## Why is this?
I rage-quit editing raw HTML and CSS, so I decided I'd create something that doesn't require me to edit raw HTML and CSS.
This is a personal project, nothing serious.
It's made specifically for my purposes, so if you want to add features of your own, just fork the damn code, will you?

## How is this?
~~Pure Python, babyyyyyyyy~~
Pure Python + JetBrains PyCharm (god, I can't stand venv on Linux), awful string manipulation, and endurance (of pain, not to be mistaken with the French word for 'bread')

## Who is this?
...What?