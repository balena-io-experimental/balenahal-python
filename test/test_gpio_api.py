# coding: utf-8

"""
    balenahal

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import balenahal
from balenahal.api.gpio_api import GpioApi  # noqa: E501
from balenahal.rest import ApiException


class TestGpioApi(unittest.TestCase):
    """GpioApi unit test stubs"""

    def setUp(self):
        self.api = balenahal.api.gpio_api.GpioApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_export(self):
        """Test case for export

        """
        pass

    def test_get_direction(self):
        """Test case for get_direction

        """
        pass

    def test_get_value(self):
        """Test case for get_value

        """
        pass

    def test_set_direction(self):
        """Test case for set_direction

        """
        pass

    def test_set_value(self):
        """Test case for set_value

        """
        pass

    def test_unexport(self):
        """Test case for unexport

        """
        pass


if __name__ == '__main__':
    unittest.main()
