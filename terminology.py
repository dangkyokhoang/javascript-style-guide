import sys
import re

# Add terminology.md to README.md as a section thereof

with open('README.md', encoding='utf-8') as f:
    readme = f.read()
# Insertion point == before the translation section
pattern = '\\s+(## <a name="terminology"[\\s\\S]+|)## <a name="translation"'

match = re.search(pattern, readme)
if match:
    with open('terminology.md', encoding='utf-8') as f:
        terminology = f.read().strip()
    # The range (start, end) is to be replaced
    start = match.start()
    #     with the translation section excluded
    end = match.end(1)

    with open('README.md', 'w', encoding='utf-8', newline='\n') as f:
        f.write('{}\n\n{}\n\n{}\n\n{}'.format(
            readme[:start],
            terminology,
            '**[⬆ về đầu trang](#table-of-contents)**',
            readme[end:]))
else:
    # Where to insert the terminology section by now?
    sys.exit(1)
