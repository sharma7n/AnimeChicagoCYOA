import re

with open('show_ids.csv', 'r') as csv:
    idmap = {}
    for line in csv.readlines():
        id_, show = line.split(',\t')
        idmap[show[:-1]] = id_


with open('templates/cyoa2.html', 'w') as new, open('templates/cyoa.html', 'r') as old:
    regex = re.compile(r'(You should watch &#39;&#39;)(.+?)(&#39;&#39;.)')
    for line in old.readlines():
        match = regex.search(line)
        if match:
            title = match.group(2)
            title_id = idmap[title]
            to_sub = f"Open #{title_id}"
            subbed = re.sub(r'(You should watch &#39;&#39;)(.+?)(&#39;&#39;.)', to_sub, line)
            new.write(subbed)
        else:
            new.write(line)