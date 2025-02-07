from setuptools import setup, find_packages

setup(
    name="litgit",
    version="0.1",
    packages=find_packages(),  # Automatically find the `litgit` package
    entry_points={
        "console_scripts": [
            "litgit = litgit.litgit:main",  # Entry point for the `litgit` command
        ],
    },
)
