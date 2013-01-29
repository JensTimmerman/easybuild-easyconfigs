##
# Copyright 2013 Ghent University
#
# This file is part of EasyBuild,
# originally created by the HPC team of Ghent University (http://ugent.be/hpc/en),
# with support of Ghent University (http://ugent.be/hpc),
# the Flemish Supercomputer Centre (VSC) (https://vscentrum.be/nl/en),
# the Hercules foundation (http://www.herculesstichting.be/in_English)
# and the Department of Economy, Science and Innovation (EWI) (http://www.ewi-vlaanderen.be/en).
#
# http://github.com/hpcugent/easybuild
#
# EasyBuild is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation v2.
#
# EasyBuild is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EasyBuild.  If not, see <http://www.gnu.org/licenses/>.
##
"""
@author: Jens Timmerman
this module contains unit tests for easyblock
"""
import os
import re
import shutil
import tempfile
import sys

from easybuild.framework.easyblock import EasyBlock
from easybuild.tools import config
from unittest import TestCase, TestLoader
from easybuild.tools.build_log import EasyBuildError


class EasyConfigTest(TestCase):
    """ Baseclass for easyblock testcases """

    def setUp(self):
        """ setup """
        pass

    def test_easyconfigs(self):
        """ make sure all easyconfigs work"""
        # self.assertRaises(NotImplementedError, eb.run_all_steps, True, False)
        # self.assertErrorRegex(EasyBuildError, "No default extension class set", eb.extensions_step)
        # self.assertTrue('ext1' in [y for x in eb.exts for y in x.values()])
        # self.assertFalse('ext2' in [y for x in eb.exts for y in x.values()])
        pass

    def tearDown(self):
        """ make sure to remove the temporary file """
        pass

    def assertErrorRegex(self, error, regex, call, *args):
        """ convenience method to match regex with the error message """
        try:
            call(*args)
            self.assertTrue(False)  # this will fail when no exception is thrown at all
        except error, err:
            res = re.search(regex, err.msg)
            if not res:
                print "err: %s" % err
            self.assertTrue(res)


def suite():
    """ return all the tests in this file """
    return TestLoader().loadTestsFromTestCase(EasyConfigTest)

