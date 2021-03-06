from setuptools import setup

# grab metadata
version = '1.00'
with open('winstats.py') as f:
    for line in f:
        if line.lstrip().startswith('__version__'):
            try:
                version = line.split("'")[1]
            except IndexError:  pass
            break

# readme is needed at register time, not install time
try:
    with open('readme.rst') as f:  # won't accept unicode on older versions :/
        long_description = f.read().decode('utf8').encode('ascii', 'replace')
except AttributeError:
    with open('readme.rst') as f:  # py3
        long_description = f.read()
except IOError:
    long_description = ''


setup(
    name          = 'winstats',
    version       = version,
    description   = 'A simple Windows status retrieval module ' +
                    'with no additional dependencies.',
    author        = 'Mike Miller',
    author_email  = 'mixmastamyk@bitbucket.org',
    url           = 'https://github.com/mixmastamyk/winstats',
    py_modules    = ['winstats'],

    long_description = long_description,
    classifiers     = [
        'Development Status :: 4 - Beta',
        'Environment :: Win32 (MS Windows)',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
        'Operating System :: Microsoft :: Windows :: Windows 7',
        'Operating System :: Microsoft :: Windows :: Windows XP',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Topic :: System :: Hardware',
        'Topic :: System :: Monitoring',
        'Topic :: System :: Systems Administration',
        'Topic :: Software Development :: Libraries',
    ],
)
