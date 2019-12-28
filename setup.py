from setuptools import setup

setup(
    name='PyInstagramAPI',
    version='1.0.2',
    description='Unofficial instagram API, provides you with access to ALL'
                ' Instagram features.',
    url='https://github.com/sgilissen/Instagram-API-python',
    author='Steve Gilissen',
    author_email='steve.gilissen@gmail.com',
    license='GNU',
    packages=['PyInstagramAPI'],
    zip_safe=False,
    install_requires=[
        "requests",
        "requests-toolbelt",
        "moviepy",
        "pycurl"
    ])
