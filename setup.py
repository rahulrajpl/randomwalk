from setuptools import setup, find_packages

setup(
    name='randomwalk_package',            # The name of your package
    version='0.1.1',                  # Initial release version
    description='A command line tool to display a resume with colorful typewriter effect.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Rahul Raj',
    author_email='rahulrajpl@gmail.com',
    url='https://github.com/rahulrajpl/randomwalk',  # Project URL
    packages=find_packages(),
    install_requires=[
        'rich'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'resume-display=resume_package.resume:main',
        ],
    },
)
