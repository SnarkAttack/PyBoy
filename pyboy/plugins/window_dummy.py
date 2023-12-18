#
# License: See LICENSE.md file
# GitHub: https://github.com/Baekalfen/PyBoy
#

import pyboy
from pyboy import utils
from pyboy.plugins.base_plugin import PyBoyWindowPlugin

logger = pyboy.logging.get_logger(__name__)


class WindowDummy(PyBoyWindowPlugin):
    name = "dummy"

    def __init__(self, pyboy, mb, pyboy_argv):
        super().__init__(pyboy, mb, pyboy_argv)

        pyboy._rendering(False)

    @classmethod
    def enabled(cls, pyboy, pyboy_argv):
        return pyboy_argv.get("window_type") == "dummy"

    def set_title(self, title):
        logger.debug(title)
