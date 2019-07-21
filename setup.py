from setuptools import setup, find_packages

setup(
    name='spotify-videoclips',
    version='1.2.2',
    packages=find_packages(include=[
        'spotify-videoclips', 'spotify-videoclips.*'
    ]),
    description='Simple tool to show Youtube videoclips and lyrics for the playing Spotify songs',
    url='https://github.com/marioortizmanero/spotify-videoclips',
    license='MIT',
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    author='Mario O.M.',
    author_email='marioortizmanero@gmail.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Multimedia :: Sound/Audio :: Players',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='spotify videoclip videoclips video videos lyrics',
    python_requires='>=3.5',
    install_requires=[
        'youtube-dl',
        'python-vlc',
        'lyricwikia'
        ],
    entry_points={
        'console_scripts' : [ 'spotify-videoclips = src.spotify_videoclips:main' ]
    }
)