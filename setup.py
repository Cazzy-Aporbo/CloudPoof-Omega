from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="cloudpoof-omega",
    version="1.0.0",
    author="Cazandra Aporbo MS",
    author_email="becaziam@gmail.com",
    description="The consciousness that thinks 20 steps ahead",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Cazzy-Aporbo/CloudPoof-Omega",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
    install_requires=[
        "numpy>=1.24.3",
        "fastapi>=0.103.0",
        "uvicorn>=0.23.2",
        "aiohttp>=3.8.5",
        "pydantic>=2.3.0",
        "rich>=13.5.2",
    ],
    entry_points={
        "console_scripts": [
            "cloudpoof=cloudpoof_core:awaken",
            "cloudpoof-server=api.server:run",
        ],
    },
)
