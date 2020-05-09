from setuptools import setup

from xlrd2.info import __VERSION__

setup(
    name = 'xlrd2',
    version = __VERSION__,
    author = 'Amirreza Niakanlahiji',
    author_email = 'aniak2@uis.edu',
    packages = ['xlrd2'],
    scripts = [
        'scripts/runxlrd2.py',
    ],
    description = (
        'Library for developers to extract data from '
        'Microsoft Excel (tm) spreadsheet files'
    ),
    long_description = (
        "Extract data from Excel spreadsheets "
        "(.xls and .xlsx, versions 2.0 onwards) on any platform. "
        "Pure Python (2.7, 3.4+). "
        "Strong support for Excel dates. Unicode-aware."
    ),
    platforms = ["Any platform -- don't need Windows"],
    license = 'Apache License 2.0',
    keywords = ['xls', 'excel', 'spreadsheet', 'workbook'],
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Operating System :: OS Independent',
        'Topic :: Database',
        'Topic :: Office/Business',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
)