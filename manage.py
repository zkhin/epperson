#!/usr/bin/env python
import os
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)))
def run(args):
    os.environ["DJANGO_SETTINGS_MODULE"] = "epperson.settings"
    from django.core.management import execute_from_command_line as execute
    execute(['manage.py'] + args)

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'epperson.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
