# -*- coding: utf-8 -*-
"""Content-oriented XBlocks."""

from string import Template  # pylint: disable=W0402

from lxml import etree

from xblock.core import XBlock, String, Scope
from xblock.fragment import Fragment


class HelloWorldBlock(XBlock):
    """A simple block: just show some fixed content."""

    def fallback_view(self, view_name, context=None):  # pylint: disable=W0613
        """Provide a fallback view handler"""
        return Fragment(u"Hello, World!")

    @staticmethod
    def workbench_scenarios():
        return [
            ("Hello World", "<helloworld_demo/>")
        ]