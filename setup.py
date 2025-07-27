# setup.py
from setuptools import setup, find_packages

setup(
    name="emotion_detection",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "transformers",
        "torch"
    ],
    author="Your Name",
    description="Emotion detection using transformers",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown"
)
