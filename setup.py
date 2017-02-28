# coding=utf-8
import os

from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

SHORT_DESCRIPTION = ('Django application to provide an internal communication channel for django projects through a '
                     'tickets system')

setup(
    name='django-icc',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description=SHORT_DESCRIPTION,
    long_description=README,
    url='https://github.com/Belco90/django-icc',
    author='Mario Beltrán Alarcón',
    author_email='belco90@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.10',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
