# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import locale
import logging
import os
from subprocess import PIPE, Popen


def minimal_logger(name):
    log = logging.getLogger(name)
    formatter = logging.Formatter(
        "%(asctime)s IFCFG DEBUG : %(name)s : %(message)s"
    )
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    console.setLevel(logging.DEBUG)

    if 'IFCFG_DEBUG' in os.environ.keys() and os.environ['IFCFG_DEBUG'] == '1':
        log.setLevel(logging.DEBUG)
        log.addHandler(console)
    return log

def exec_cmd(cmd_args):
    # Using `shell=True` because commands may be scripts
    # Using `universal_newlines=True` because we want string output, not bytes
    proc = Popen(cmd_args, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    stdout, stderr = proc.communicate()
    proc.wait()
    # If we aren't using UTF-8 on this system, then re-encode the string.
    if locale.getpreferredencoding().lower() != "utf-8":
        stdout = stdout.decode(locale.getpreferredencoding()).encode('utf-8')
        stderr = stderr.decode(locale.getpreferredencoding()).encode('utf-8')
    return (stdout, stderr, proc.returncode)

def hex2dotted(hex_num):
    num = hex_num.split('x')[1]
    w = int(num[0:2], 16)
    x = int(num[2:4], 16)
    y = int(num[4:6], 16)
    z = int(num[6:8], 16)

    return "%d.%d.%d.%d" % (w, x, y, z)
