""" Defines text processing transformations to be used by the CLI. """

import re


def recommend_to_id(lines):
    """ Linewise transforms "You should watch {show}" to "Open #{id(show)}" """
    
    # get show ids from titles
    with open('show_ids.csv', 'r') as csv:
        idmap = {}
        for line in csv.readlines():
            id_, show = line.split(',\t')
            idmap[show[:-1]] = id_
    
    # yield modified lines
    regex = re.compile(r'(You should watch &#39;&#39;)(.+?)(&#39;&#39;.)')
    for line in lines:
        match = regex.search(line)
        if match:
            title = match.group(2)
            title_id = idmap[title]
            subbed = regex.sub(f"Open #{title_id}", line)
            yield subbed
        else:
            yield line

def id_to_drawer(lines):
    """ Linewise transforms "Open #{id}" to "Open drawer #{id}" """
    
    regex = re.compile(r'Open\ \#(?P<title_id>\d+)')
    
    for line in lines:
        match = regex.search(line)
        if match:
            title_id = match.group('title_id')
            yield regex.sub(f"Open drawer #{title_id}", line)
        else:
            yield line

def get_generator_function(name):
    return {
        'recommend_to_id': recommend_to_id,
        'id_to_drawer': id_to_drawer,
    }[name]