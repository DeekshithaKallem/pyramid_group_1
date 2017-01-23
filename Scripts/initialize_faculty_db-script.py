#!c:\users\sa\desktop\python_proj\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'faculty','console_scripts','initialize_faculty_db'
__requires__ = 'faculty'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('faculty', 'console_scripts', 'initialize_faculty_db')()
    )
