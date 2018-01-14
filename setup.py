from setuptools import setup

setup(
    name             = 'primes',
    packages         = ['primes',],
    install_requires = ['isqrt',],
    license          = 'MIT',
    url              = 'https://github.com/lapets/primes',
    author           = 'Andrei Lapets',
    author_email     = 'a@lapets.io',
    description      = 'Python library encapsulating the set of all primes as an indexed collection (optimized for small primes).',
    long_description = open('README.rst').read(),
    test_suite       = 'nose.collector',
    tests_require    = ['nose'],
    include_package_data = True,
)
