#!/usr/bin/env python
import os
import sys
from os.path import dirname, abspath

if __name__ == "__main__":
    SITE_ROOT = dirname(abspath(__file__))
    sys.path.append(SITE_ROOT)
    os.environ["DJANGO_SETTINGS_MODULE"] = "settings.local"

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
