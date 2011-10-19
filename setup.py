from setuptools import setup, find_packages

setup(
    name='sphc',
    version='0.8.6',
    description='Simple Pythonic HTML Creator',
    long_description=open("README.rst").read(),
    packages=find_packages(),
    author='Shekhar Tiwatne',
    author_email='pythonic@gmail.com',
    url="http://flavors.me/shon",
    license="http://www.opensource.org/licenses/mit-license.php",
    requires=['pytidylib']
    )

