#!/usr/bin/python
#-*- coding: utf-8 -*-
import re
import os
import datetime
import argparse

from collections import OrderedDict
from slugify import UniqueSlugify

BASE_DIR = os.path.dirname(__file__)
CONTENT_DIR = os.path.join(BASE_DIR, 'content')

empty_string = re.compile('\s')


class SlugUIDS(object):
    def __init__(self, fname):
        self.category = self.get_category_name(fname)
        self.category_dir = os.path.join(CONTENT_DIR, self.category)
        self.uids = self.get_uids()

    def get_file_slug(self, fname):
        with open(fname, 'rb') as f:
            for line in f.readlines():
                if line.startswith('Slug'):
                    slugs = re.findall('Slug: (\w+)', line)
                    return slugs
                elif empty_string.match(line):
                    break
        return []

    def get_files_slug(self, uids, dirname, fnames):
        for fname in fnames:
            fname = os.path.join(dirname, fname)
            slugs = self.get_file_slug(fname)
            uids.extend(slugs)
        return uids

    def get_uids(self):
        uids = []
        os.path.walk(self.category_dir, self.get_files_slug, uids)
        return uids

    def get_category_name(self, fname):
        return os.path.split(os.path.dirname(fname))[1]


class TxtParser(object):
    def __init__(self, fname, slug_uids):
        self.fname = fname
        self.slug_uids = slug_uids
        self.category = self.slug_uids.category
        self.category_dir = self.slug_uids.category_dir
        with open(fname) as f:
            self.title = f.readline().strip().decode('utf-8')
            self.summary = f.readline().strip().decode('utf-8')
            self.data = '\n'.join([l.strip().decode('utf-8') for l in f.readlines()])
        self.slug = UniqueSlugify(to_lower=True, separator='_', uids=slug_uids.uids)


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

    def generate_result(self):
        self.set_header()
        self.set_output_filename()
        self.set_content()

    def save_result(self):
        self.generate_result()
        # TODO: make check if file exists before write
        with open(os.path.join(self.txt_parser.category_dir, self.filename), 'wb') as f:
            f.write(self.header.encode('utf-8'))
            f.write(u'\n\n')
            f.write(self.content.encode('utf-8'))
            print u'Output file: %r' % f.name

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process file.')
    parser.add_argument('filename', metavar='f', type=str, help='file to parse')
    args = parser.parse_args()

    fname = args.filename
    slug_uids = SlugUIDS(fname)
    txt_parser = TxtParser(fname, slug_uids)

    mdgen = MdGenerator(txt_parser)
    mdgen.save_result()

