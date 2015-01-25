from setuptools import find_packages,setup


setup(
        name='aurtools',
        version='1.0',
        author="Matthew Raspberry",
        author_email="nixalot@nixalot.com",
        url='https://github.com/nixalot/aurtools',
        description="Tools for searching and downloading packages from the Arch Linux AUR",
        install_requires=['requests'],
        packages=find_packages(),
        entry_points={
            'console_scripts':[
                'aurdownload = aurtools:aurdownload',
                'aursearch = aurtools:aursearch',
                ]
            }
        )

