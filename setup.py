from setuptools import setup

setup(
    name='python-cephclient',
    packages=['cephclient'],
    version='0.1.0.5',
    url='https://github.com/dmsimard/python-cephclient',
    author='David Moreau Simard',
    author_email='moi@dmsimard.com',
    description='A client library in python for the Ceph REST API.',
    long_description=open('README.rst', 'rt').read(),
    license='Apache License, Version 2.0',
    keywords='ceph rest api ceph-rest-api client library',
    install_requires=['lxml>=3.2.5', 'requests>=2.2.1'],
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Information Technology',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities'
    ]
)
