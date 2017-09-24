from setuptools import setup, find_packages

setup(
    name='epsilon',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'Colorama',
        'BeautifulSoup4',
        'Psutil',
        'Discord',
        'Asyncio',
        'Mss',
        
    ],
    entry_points='''
        [console_scripts]
        epsilon=epsilon:cli
    ''',
)