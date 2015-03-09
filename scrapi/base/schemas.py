from __future__ import unicode_literals

from copy import deepcopy

from nameparser import HumanName


def default_name_parser(names):
    names = names.split(';')

    contributor_list = []
    for person in names:
        name = HumanName(person)
        contributor = {
            'prefix': name.title,
            'given': name.first,
            'middle': name.middle,
            'family': name.last,
            'suffix': name.suffix,
            'email': '',
            'ORCID': ''
        }
        contributor_list.append(contributor)

    return contributor_list


def format_tags(all_tags):
    tags = []
    for taglist in all_tags.split(' '):
        tags += taglist.split(',')

    return list(set([unicode(tag.lower().strip()) for tag in tags if tag.lower().strip()]))


def update_schema(old, new):
    d = deepcopy(old)
    for key, value in new.items():
        d[key] = value
    return d


BASEXMLSCHEMA = {
    "description": ['//dc:description/node()', unicode],
    "contributors": ['//dc:creator/node()', default_name_parser],
    "title": ['//dc:title/node()', unicode],
    "dateUpdated": ['//dc:dateEntry/node()', unicode],
    "id": {
        "url": ['//dcq:identifier-citation/node()', unicode],
        "serviceID": ['//dc:ostiId/node()', unicode],
        "doi": ['//dc:doi/node()', unicode]
    },
    "tags": ['//dc:subject/node()', format_tags]
}
