# -*- coding: utf-8 -*-
"""
Tests that don't mock anything, just run on the host system.
"""
from __future__ import unicode_literals

import ifcfg

from .base import IfcfgTestCase


class IfcfgTestCase(IfcfgTestCase):

    def test_ifcfg(self):
        for interface in ifcfg.interfaces():
            print(interface)
