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
    def get_files(self):
        s = sig.SIG("./examples", "./examples/build")
        s.run()
        return s

    # -------------------------------------------------------------------------------
    #
    def get_topic(self, topic: str, d: list):
        t = None
        for x in d:
            if x.name == topic:
                t = x
                break

        return t

    # -------------------------------------------------------------------------------
    #
    def test_bool(self):
        # Find the files
        s = self.get_files()
        d = s.get_data()

        # Find the Boolean topic
        t = self.get_topic("test_bool_topic", d)

        # Test the data in the topic `t`
        self.assertEqual(t.data["bool"][0].name, "my_false")
        self.assertEqual(t.data["bool"][1].name, "my_true")
        self.assertEqual(t.data["bool"][2].name, "my_bool")

        self.assertEqual(t.data["bool"][0].get_value(), False)
        self.assertEqual(t.data["bool"][1].get_value(), True)
        self.assertEqual(t.data["bool"][2].get_value(), True)

        return

    # -------------------------------------------------------------------------------
    #
    def test_float(self):
        # Find the files
        d = self.get_files()
        f = d.get_files()
        return

    # -------------------------------------------------------------------------------
    #
    def test_int(self):
        # Find the files
        d = self.get_files()
        f = d.get_files()
        return

    # -------------------------------------------------------------------------------
    #
    def test_list(self):
        # Find the files
        d = self.get_files()
        f = d.get_files()
        return

    # -------------------------------------------------------------------------------
    #
    def test_str(self):
        # Find the files
        d = self.get_files()
        f = d.get_files()
        return
