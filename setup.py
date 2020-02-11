import setuptools

HEUSLER_MPL_STYLE = 'heuslertools/plotting/heusler.mplstyle'

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="heuslertools",
    version="0.0.2",
    author="Lukas Scheffler",
    author_email="lukas.scheffler@physik.uni-wuerzburg.de",
    description="Useful tools for daily work with Heusler stuff.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    install_requires=['matplotlib',
                      'numpy',
                      'scipy',
                      'periodictable',
                      'tabulate',
                      'pyinstaller',
                      'scikit-image'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)

# import matplotlib
# from shutil import copyfile
# import os
#
# copyfile(HEUSLER_MPL_STYLE, os.path.join(matplotlib.get_configdir(),'stylelib', 'heusler.mplstyle'))
