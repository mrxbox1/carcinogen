
md_string = """# Pull and peel licorice
## bees
According to all known laws of aviation, there is no way a bee should be able to fly.
### bees2
Its wings are too fat to lift its fat little body off the ground.
#### bees3
The bee, of course, flies anyway.
##### bees4
Because bees don't care what humans think is possible.
###### bees5
Yellow, black, yellow, black, yellow, black, yellow, black...Ooh! Black and yellow! Let's shake it up a little!"""

def md_to_html(string):
    string = string.split("\n")
    final_html = "<html><body>"

    for line in string:
        if line.startswith("#"):

            # gotta count all the hashes to determine the heading
            hash_count = 0
            for char in line[:7]:
                if char == '#':
                    hash_count += 1

            final_html += f'<h{hash_count}>' + line.replace('#', '') + f'</h{hash_count}>'

        else:
            final_html += '<p>' + line + '</p>'

    final_html += '</body></html>'

    return final_html

if __name__ == "__main__":
    # test functionality
    print(md_to_html(md_string))