# Copyright: 2006 Marien Zwart <marienz@gentoo.org>
# License: BSD/GPL2

from pkgcore import plugins
from pkgcore.scripts import pplugincache
from pkgcore.test import TestCase
from pkgcore.test.scripts.helpers import ArgParseMixin


class CommandlineTest(TestCase, ArgParseMixin):

    _argparser = pplugincache.argparser

    has_config = False

    def test_parser(self):
        self.assertEqual([plugins], self.parse().packages)
