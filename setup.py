from distutils.core import setup

setup(
   name="bob",
   version="0.1.0",
   author="Calum J. Eadie",
   packages=["bob"],
   license=open("LICENSE.txt").read(),
   description="Really simple Python build tool.",
   long_description=open("README.md").read(),
   install_requires=[],
)
