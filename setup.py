from setuptools import setup, find_packages


setup(
    name='word_counter',
    version='0.1',
    author_email='radzhome@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/radlws/python-word-counter',
    license='',
    description='A simple word counter.',
    long_description=open('README.md').read(),
    zip_safe=False,
)
