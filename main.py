
md_sample = open('sample.md', 'r').readlines()

def md_to_html(md_text):
    final_html = "<!DOCTYPE html><html><body>"

    for line in md_text:
        if line.startswith("#"):

            # gotta count all the hashes to determine the heading
            hash_count = 0
            for char in line[:7]:
                if char == '#':
                    hash_count += 1

            final_html += f'<h{hash_count}>' + line.replace('#', '') + f'</h{hash_count}>'

        else:
            final_html += '<p>' + line + '</p>'

    final_html += "</body></html>"

    return final_html

if __name__ == "__main__":
    # test functionality
    print(md_to_html(md_sample))