import unittest

import ifcfg


class IfcfgTestCase(unittest.TestCase):
    """
    Basic test class, just makes sure to restore the original module-wide
    properties of ifcfg
    """

    def setUp(self):
        self.old_platform = ifcfg.platform
        self.old_parser_class = ifcfg.Parser

    def tearDown(self):
        ifcfg.platform = self.old_platform
        ifcfg.Parser = self.old_parser_class
