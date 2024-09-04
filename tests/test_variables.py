#!/usr/bin/python

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Standard Lib
import SIG.sig as sig
import os
import unittest

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Packages

# ===============================================================================
#


class TestVariables(unittest.TestCase):
    # -------------------------------------------------------------------------------
    #
    def get_files():
        d = sig.SIG("./examples", "./examples/build")
        d.run()
        return d

    # -------------------------------------------------------------------------------
    #
    def test_bool(self):
        # Find the files
        d = TestVariables.get_files()
        f = d.get_files()

    # -------------------------------------------------------------------------------
    #
    def test_float(self):
        # Find the files
        d = TestVariables.get_files()
        f = d.get_files()

    # -------------------------------------------------------------------------------
    #
    def test_int(self):
        # Find the files
        d = TestVariables.get_files()
        f = d.get_files()

    # -------------------------------------------------------------------------------
    #
    def test_list(self):
        # Find the files
        d = TestVariables.get_files()
        f = d.get_files()

    # -------------------------------------------------------------------------------
    #
    def test_str(self):
        # Find the files
        d = TestVariables.get_files()
        f = d.get_files()
