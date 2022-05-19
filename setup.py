from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="pokemon",
    version="0.0.1",
    author="Manoel Rodrigues do Nascimento",
    author_email="jiujitsu30@gmail.com",
    description="The RESTful Pokémon API",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Manoel/pacoteDio"
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)