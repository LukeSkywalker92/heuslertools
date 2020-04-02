import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="heuslertools",
    version="0.0.4",
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
                      'scikit-image',
                      'Pillow',
                      'lmfit',
                      'h5py'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    scripts=['programs/generateRHEEDvideo/generateRHEEDvideo',
             'programs/gamma/gamma.py',
             'programs/plot_squid/plot_squid.py',
             'programs/rheed_oszi/rheed_oszi.py'],
)
