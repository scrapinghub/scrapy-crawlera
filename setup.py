from setuptools import setup

with open("README.rst") as f:
    readme = f.read()


setup(
    name='scrapy-zyte-smartproxy',
    version='2.3.3',
    license='BSD',
    description='Scrapy middleware for Zyte Smart Proxy Manager',
    long_description=readme,
    maintainer='Raul Gallegos',
    maintainer_email='raul.ogh@gmail.com',
    author='Zyte',
    author_email='opensource@zyte.com',
    url='https://github.com/scrapy-plugins/scrapy-zyte-smartproxy',
    packages=['scrapy_zyte_smartproxy'],
    python_requires='>=3.8',
    install_requires=['scrapy>=1.4.0', 'six', 'w3lib'],
    platforms=['Any'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Framework :: Scrapy',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: Proxy Servers',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
