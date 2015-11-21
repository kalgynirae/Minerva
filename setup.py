from setuptools import setup

setup(
    name = 'minerva',
    packages = ['minerva'],
    entry_points = {
        'console_scripts': 'minerva = minerva.main',
    },
)
