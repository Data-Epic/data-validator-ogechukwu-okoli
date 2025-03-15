from setuptools import setup, find_packages

setup(
    name='datavalidatorpro',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3.13.2',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)