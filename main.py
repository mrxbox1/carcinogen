CURRENT_VERSION = "0.1 (2026-05-31)"

md_sample = open('sample.md', 'r').readlines()

"""
Converts any MD file into HTML.
Parameter md_text should be a list of lines in the MD file (provided ideally using Python's open('[FILE]', 'r').readlines() function)
"""
def md_to_html(md_text):
    final_html = "<!-- Made with Carcinogen " + CURRENT_VERSION + " --><!DOCTYPE html><html><body>"

    for line in md_text:

        ### URLS ARE NOT HANDLED HERE, FUCK OFF
        #for word in line:
        #    if word == r'https:\/\/[^\s]+$':
        #        line.replace(word, f'<a href="{word}">{word}</a>')


        ### HEADINGS ARE HANDLED HERE
        if line.startswith("#"):
            # gotta count all the hashes to determine the heading
            hash_count = 0
            for char in line[:7]:
                if char == '#':
                    hash_count += 1

            final_html += f'<h{hash_count}>' + line.replace('#', '')[1:] + f'</h{hash_count}>'


        ### QUOTES ARE HANDLED HERE
        elif line.startswith('>'):
            final_html += '<q>' + line.replace('>', '')[1:] + '</q>'


        ### PARAGRAPHS ARE HANDLED HERE
        elif line.startswith('\\'):
            final_html += '<p>' + line + '</p>'
        else:
            final_html += '<p>' + line + '</p>'

    final_html += "</body></html>"

    return final_html

if __name__ == "__main__":
    # test the functionality of this by putting it in an about:blank page
    # Inspect -> edit HTML ->
    print(md_to_html(md_sample))