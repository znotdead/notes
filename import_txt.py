#!/usr/bin/python
#-*- coding: utf-8 -*-
import re
import os
import datetime
import argparse

from collections import OrderedDict, defaultdict
from slugify import UniqueSlugify

BASE_DIR = os.path.realpath(os.path.dirname(__file__))
CONTENT_DIR = os.path.join(BASE_DIR, 'content')

EXCEPT_DIRS = ['static', ]

empty_string = re.compile('\s')


class SlugUIDS(object):
    '''
    Class collects all slugs for each category for unique slugify.
    '''
    __instance = None
    def __init__(self):
        if SlugUIDS.__instance:
            raise SlugUIDS.__instance
        SlugUIDS.__instance = self

        self.uids = self._get_uids()

    def _get_file_slug(self, fname):
        with open(fname, 'rb') as f:
            for line in f.readlines():
                if line.startswith('Slug'):
                    slugs = re.findall('Slug: (\w+)', line)
                    return slugs
                elif empty_string.match(line):
                    break
        return []

    def _get_slugs_for_category(self, category_dir):
        slugs = []
        for fname in os.listdir(category_dir):
            full_name = os.path.join(category_dir, fname)
            if os.path.isfile(full_name):
                slugs.extend(self._get_file_slug(full_name))
        return slugs


    def _get_uids(self):
        uids = defaultdict(list)
        for category in os.listdir(CONTENT_DIR):
            category_dir = os.path.join(CONTENT_DIR, category)
            if category not in EXCEPT_DIRS and os.path.isdir(category_dir):
                uids[category].extend(self._get_slugs_for_category(category_dir))
        return uids


class TxtParser(object):
    '''
    Parsed file object with additional info for generator.
    '''
    def __init__(self, fname, slug_uids):
        self.full_name = os.path.normpath(fname)
        self.category_dir, self.fname = os.path.split(self.full_name)
        self.category = os.path.split(self.category_dir)[1]
        self.slug_uids = slug_uids.uids[self.category]

        with open(self.full_name) as f:
            self.title = f.readline().strip().decode('utf-8')
            self.summary = f.readline().strip().decode('utf-8')
            self.data = '\n'.join([l.rstrip().decode('utf-8') for l in f.readlines()])
        self.slug = UniqueSlugify(to_lower=True, separator='_', uids=self.slug_uids)


class MdGenerator(object):
    def __init__(self, txt_parser):
        self.txt_parser = txt_parser
        self.template = OrderedDict([
            (u'Title', None),
            (u'Date', datetime.datetime.now().strftime('%Y-%m-%d %H:%M')),
            (u'Modified', None),
            (u'Category', None),
            (u'Tags', None),
            (u'Slug', None),
            (u'Lang', u'ru'),
            (u'Authors', u'znotdead'),
            (u'Summary', None),
        ])
        print self.txt_parser.title
        print self.txt_parser.summary
        self.summary_input = raw_input(u'Summary: ')
        self.tags_input = raw_input(u'Tags: ')

    def set_title(self):
        self.template[u'Title'] = self.txt_parser.title

    def set_category(self):
        self.template[u'Category'] = self.txt_parser.category.capitalize()

    def set_tags(self):
        if self.tags_input:
            tags = self.tags_input.decode('utf-8').split(',')
        else:
            tags = []
        self.template[u'Tags'] = ', '.join(tags)

    def set_slug(self):
        self.template[u'Slug'] = self.txt_parser.slug(self.template[u'Title'])

    def set_lang(self):
        # TODO
        pass

    def set_summary(self):
        if self.summary_input:
            summary = self.summary_input.decode('utf-8')
        else:
            summary = self.txt_parser.summary
        self.template[u'Summary'] = summary

    def set_output_filename(self):
        self.filename = u'%s.%s' % (self.template[u'Slug'], 'md')

    def set_content(self):
        content = [u'### %s' % self.txt_parser.title, self.txt_parser.data]
        self.content = u'\n'.join(content)

    def set_header(self):
        self.set_title()
        self.set_category()
        self.set_tags()
        self.set_slug()
        self.set_lang()
        self.set_summary()

        header_list = []
        for k, v in self.template.items():
            header_list.append(u'%s: %s' % (k, v if v else u''))
        self.header = u'\n'.join(header_list)

    def set_filepath(self):
        self.filepath = os.path.join(self.txt_parser.category_dir, self.filename)

    def generate_result(self):
        self.set_header()
        self.set_content()
        self.set_output_filename()
        self.set_filepath()

    def save_result(self):
        self.generate_result()
        # TODO: make check if file exists before write
        with open(self.filepath, 'wb') as f:
            f.write(self.header.encode('utf-8'))
            f.write(u'\n\n')
            f.write(self.content.encode('utf-8'))
            print u'Output file: %r' % f.name

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process file.')
    parser.add_argument('filename', metavar='f', type=str, help='file to parse')
    args = parser.parse_args()

    fname = args.filename
    slug_uids = SlugUIDS()
    txt_parser = TxtParser(fname, slug_uids)

    mdgen = MdGenerator(txt_parser)
    mdgen.save_result()

