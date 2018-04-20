from setuptools import setup
setup(
    name='text2midi',
    version='0.0.1',
    description='Text File To Midi File Converter',
    author='Tatsuya Matoba',
    author_email='mtb.toya0403@gmail.com',
    include_package_data=True,
    install_requires=[
        'pretty_midi',
        'pandas'
    ],
    entry_points="""
        [console_scripts]
         text2midi = text2midi:main
    """,
)
