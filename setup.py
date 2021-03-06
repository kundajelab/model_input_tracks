from setuptools import setup,find_packages
config = {
    'include_package_data': True,
    'author': 'Anna Shcherbina',
    'author_email': 'annashch@stanford.edu',
    'url': 'https://github.com/kundajelab/model_input_tracks',
    'description': 'Generate genome-wide input tracks for deep learning',
    'version': '0.1',
    'packages': [],
    'setup_requires': [],
    'install_requires': ['numpy>=1.15','pyBigWig>=0.3.6', 'pysam'],
    'scripts': [],
    'entry_points': {'console_scripts': ['make_gc_track=model_input_tracks.gc.__init__:main',
                                         'make_gc_nosmooth_track=model_input_tracks.gc_nosmooth.__init__:main',
                                         'smooth_bigwig=model_input_tracks.smooth_bigwig:main']},
    'name': 'model_input_tracks'
}

if __name__== '__main__':
    setup(**config)
