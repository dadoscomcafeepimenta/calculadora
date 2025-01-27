from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="calculadora",
    version="0.0.1",
    author="Wanessa Silva",
    author_email="dadoscomcafeepimenta@gmail.com",
    description="Projeto de teste para entender como criar pacotes",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dadoscomcafeepimenta/calculadora",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)