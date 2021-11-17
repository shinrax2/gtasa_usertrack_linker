#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# build.py for gtasa_usertrack_linker by shinrax2

import PyInstaller.__main__

args = [
    "--name=gtasa_usertrack_linker",
    "--clean",
    "--onefile",
    "main.py"
]
PyInstaller.__main__.run(args)
