from setuptools import setup, find_packages

setup(
    name='Bxss Sniper',
    version='1.0.0',
    author='D. Sanjai Kumar',
    author_email='bughunterz0047@gmail.com',
    description='Bxss Sniper: A web application penetration testing tool for Blind XSS detection',
    packages=find_packages(),
    install_requires=[
        'colorama>=0.4.4',
        'httpx>=0.25.0',
        'requests>=2.31.0'
    ],
    entry_points={
        'console_scripts': [
            'bxsniper = bxss_sniper.bxss_sniper:main',
        ],
    },
)