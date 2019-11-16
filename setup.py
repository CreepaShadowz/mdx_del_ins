#!/usr/bin/env python


from setuptools import setup


setup(
    name='mdx_del_ins',
    version='2.0',
    author='Alexandre Leray',
    author_email='alexandre@stdin.fr',
    description='Python-Markdown extension to support the <del> and <ins> tags.',
    maintainer="Alphaeus",
    url='https://github.com/CreepaShadowz/mdx_del_ins',
    py_modules=['mdx_del_ins'],
    install_requires=['Markdown ~= 3.0',],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: Markup :: HTML'
    ]
)
