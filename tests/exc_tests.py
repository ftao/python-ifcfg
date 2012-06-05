"""Tests for ifcfg.exc."""

import os
import ifcfg
from nose.tools import eq_, raises

@raises(ifcfg.exc.IfcfgError)
def test_error():
    try:
        raise ifcfg.exc.IfcfgError('Error Msg')
    except ifcfg.exc.IfcfgError as e:
        eq_(e.msg, 'Error Msg')
        raise

@raises(ifcfg.exc.IfcfgParserError)
def test_error():
    try:
        raise ifcfg.exc.IfcfgParserError('Error Msg')
    except ifcfg.exc.IfcfgParserError as e:
        eq_(e.msg, 'Error Msg')
        raise