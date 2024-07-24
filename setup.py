from setuptools import setup, find_packages

setup(
    name='base64_encoder',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': []
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A simple base64 encoder and decoder with salt key and index.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/base64_encoder',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
