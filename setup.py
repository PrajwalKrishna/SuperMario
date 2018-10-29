from distutils.core import setup
import setuptools

setup(
    name = 'SuperMario',
    version = '1.0',
    package_dir = {'':'.'},
    packages = setuptools.find_packages('.'),
    test_suite = 'pytest',
    tests_require = ['Pytest'],
)
