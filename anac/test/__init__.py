# Copyright (C) 2015 Leandro Lisboa Penz <lpenz@lpenz.org>
# This file is subject to the terms and conditions defined in
# file 'LICENSE.txt', which is part of this source code package.

import unittest
import anac


class TestBasic(unittest.TestCase):

    def test_import(self):
        try:
            anac.Anac()
        except:
            pass
