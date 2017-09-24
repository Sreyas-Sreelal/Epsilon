from setuptools import setup, find_packages

setup(
    name='epsilon',
    version='1.0',
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    include_package_data=True,
    install_requires=[
        'Colorama',
        'BeautifulSoup4',
        'Psutil',
        'Discord',
        'Asyncio',
        'Mss',
    ],
    entry_points='''
        [console_scripts]
        epsilon=epsilon:start_epsilon
    ''',
)