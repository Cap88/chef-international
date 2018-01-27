from setuptools import setup

setup(
    name='Chef Internional',
    packages=['chef'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)