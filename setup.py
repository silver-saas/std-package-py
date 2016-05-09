from glob import glob
from os.path import basename
from os.path import splitext

from setuptools import find_packages
from setuptools import setup


def readme():
    with open('README.md') as readme_file:
        return readme_file.read()


setup(
    name='$$PACKAGE_NAME',
    version='$$VERSION',
    description='$$DESCRIPTION',
    long_description=readme(),
    keywords='$$KEYWORDS',
    url='http://github.com/silver-saas/$$PACKAGE_NAME',
    author='Horia Coman',
    author_email='horia141@gmail.com',
    license='All right reserved',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    install_requires=[
        # For testing
        ],
    test_suite='tests',
    tests_require=[],
    include_package_data=True,
    zip_safe=False
)
