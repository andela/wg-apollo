#!/usr/bin/env python
import sys

import os
from django.core.management import execute_from_command_line

from tasks import (
    setup_django_environment,
    get_user_config_path
)

if __name__ == "__main__":

    # If user passed the settings flag ignore the default wger settings
    if not any('--settings' in s for s in sys.argv):
        BASE_DIR = os.path.abspath(os.path.dirname(__file__))

        setup_django_environment(os.path.join(BASE_DIR, 'settings.py'))

    # Alternative to above
    # os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

    execute_from_command_line(sys.argv)
