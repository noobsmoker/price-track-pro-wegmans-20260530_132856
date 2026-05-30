from setuptools import setup, find_packages

setup(
    name="price-track-pro-wegmans-20260530_132856",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'price=price:main',
        ],
    },
)
