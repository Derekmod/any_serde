from setuptools import find_packages, setup

setup(
    name="any_serde",
    version="0.0.4",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)
