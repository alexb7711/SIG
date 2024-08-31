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


class TestSIG(unittest.TestCase):
    # -------------------------------------------------------------------------------
    #
    def get_files():
        d = sig.SIG("./example", "None")
        d.run()
        return d

    # -------------------------------------------------------------------------------
    #
    def test_dir_search(self):
        # Find the files
        d = TestSIG.get_files()
        f = d.get_files()

        # Count the files
        self.assertEqual(len(f["pub"]), 1)
        self.assertEqual(len(f["sub"]), 1)
        self.assertEqual(len(f["mock"]), 1)

        # Check file names
        pwd = os.path.abspath("./example")

        self.assertEqual(pwd + "/publishers/pub_position.yml", f["pub"][0])
        self.assertEqual(pwd + "/subscribers/sub_position.yml", f["sub"][0])
        self.assertEqual(pwd + "/mock/mock_dc_motor.yml", f["mock"][0])

        return

    # -------------------------------------------------------------------------------
    #
    def test_first_level_data_structure(self):
        # Find the files
        d = TestSIG.get_files()
        f = d.get_data()

        # Publisher
        self.assertEqual(f["pub"][0].name, "test_publisher")
        self.assertTrue(isinstance(f["pub"][0].publish["int"], list))
        self.assertEqual(f["pub"][0].desc, "This is a test publisher")

        # Subscriber
        self.assertEqual(f["sub"][0].name, "test_subscriber")
        self.assertTrue(isinstance(f["sub"][0].subscriptions, list))
        self.assertEqual(f["sub"][0].desc, "This is a test subscriber")

        # Mock
        self.assertEqual(f["mock"][0].name, "test_mock")
        self.assertTrue(isinstance(f["mock"][0].data["int"], list))
        self.assertEqual(f["mock"][0].desc, "This is a test mock")
        return
