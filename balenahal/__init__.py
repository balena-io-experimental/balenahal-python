from __future__ import absolute_import
import platform
import os
from subprocess import Popen
import inspect

import balenahal.apis as apis


class Balenahal:
    def __init__(self):

        arch = platform.machine()
        file_path = os.path.dirname(os.path.realpath(__file__))
        proxy_path = file_path + "/bin/wamr-proxy-" + arch
        process = Popen([proxy_path])

        for name, obj in inspect.getmembers(apis, inspect.isclass):
            if name.endswith("Api"):
                setattr(self, name[: len(name) - 3].lower(), obj())
