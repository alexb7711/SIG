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
        s = sig.SIG("./examples", "./examples/build")
        s.run()
        return s

    # -------------------------------------------------------------------------------
    #
    def test_bool(self):
        # Find the files
        s = TestVariables.get_files()
        d = s.get_data()

        # Find the Boolean topic
        t = None
        for x in d:
            if x.name == "test_bool_topic":
                t = x
                break

        # Test the data in the topic `t`
        print(t)
        self.assertTrue(False)

        return

    # -------------------------------------------------------------------------------
    #
    def test_float(self):
        # Find the files
        d = TestVariables.get_files()
        f = d.get_files()
        return

    # -------------------------------------------------------------------------------
    #
    def test_int(self):
        # Find the files
        d = TestVariables.get_files()
        f = d.get_files()
        return

    # -------------------------------------------------------------------------------
    #
    def test_list(self):
        # Find the files
        d = TestVariables.get_files()
        f = d.get_files()
        return

    # -------------------------------------------------------------------------------
    #
    def test_str(self):
        # Find the files
        d = TestVariables.get_files()
        f = d.get_files()
        return
