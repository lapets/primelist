from setuptools import setup

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name="primelist",
    version="0.1.0.1",
    packages=["primelist",],
    install_requires=["isqrt",],
    license="MIT",
    url="https://github.com/lapets/primelist",
    author="Andrei Lapets",
    author_email="a@lapets.io",
    description="Python library encapsulating the set of all primes "+\
                "as an indexed collection (optimized for small primes).",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    test_suite="nose.collector",
    tests_require=["nose"],
    include_package_data=True,
)
