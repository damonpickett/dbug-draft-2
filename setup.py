from setuptools import setup, find_packages

setup(
    name="dbug",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "openai",
        "argparse",
        "python-dotenv"
    ],
    entry_points={
        "console_scripts": [
            "dbug = dbug.main:main",
        ]
    },
)
