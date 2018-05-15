#!/usr/bin/env python


import argparse
import os
from ruamel import yaml

from arimo.IoT.DataAdmin._project.settings import _DB_DETAILS_FILE_PATH


_DEFAULT_DB_DETAILS = yaml.safe_load(open(_DB_DETAILS_FILE_PATH, 'r'))


arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--create', action='store_true')
arg_parser.add_argument('--env')

arg_parser.add_argument('--db-eng', default=_DEFAULT_DB_DETAILS['ENGINE'])
arg_parser.add_argument('--db-host', default=_DEFAULT_DB_DETAILS['HOST'])
arg_parser.add_argument('--db-port', default=_DEFAULT_DB_DETAILS['PORT'])
arg_parser.add_argument('--db-name', default=_DEFAULT_DB_DETAILS['NAME'])
arg_parser.add_argument('--db-usr', default=_DEFAULT_DB_DETAILS['USER'])
arg_parser.add_argument('--db-pw', default=_DEFAULT_DB_DETAILS['PASSWORD'])

args = arg_parser.parse_args()


yaml.safe_dump(
    data=dict(
        ENGINE=args.db_eng,
        HOST=args.db_host,
        PORT=args.db_port,
        NAME=args.db_name,
        USER=args.db_usr,
        PASSWORD=args.db_pw),
    stream=open(_DB_DETAILS_FILE_PATH, 'w'),
    default_style=None,
    default_flow_style=False,   # collections to be always serialized in the block style
    canonical=None,
    indent=2,
    width=None,
    allow_unicode=True,
    line_break=None,
    encoding=u'utf-8',
    explicit_start=None,
    explicit_end=None,
    version=None,
    tags=None,
    block_seq_indent=None)


os.system(
    'eb {} {}'.format(
        'create' if args.create else 'deploy',
        args.env))


yaml.safe_dump(
    data=_DEFAULT_DB_DETAILS,
    stream=open(_DB_DETAILS_FILE_PATH, 'w'),
    default_style=None,
    default_flow_style=False,   # collections to be always serialized in the block style
    canonical=None,
    indent=2,
    width=None,
    allow_unicode=True,
    line_break=None,
    encoding=u'utf-8',
    explicit_start=None,
    explicit_end=None,
    version=None,
    tags=None,
    block_seq_indent=None)
