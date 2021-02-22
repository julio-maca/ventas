from setup import setup

setup(
    name='pv',
    version='0.10',
    py_modules=['pv'],
    install_requires=[
        'Click'
    ],
    entry_points='''
    [console_scripts]
    pv=pv:cli
    ''',
)