import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mind-tee",
    version="0.1.0",
    author="Mind Circuit",
    author_email="info@mindcircuit.example",
    description="A TEE-based demonstration for confidential AI and aggregator tasks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/YourOrg/mind_tee",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=[
        # Add required dependencies or rely on requirements.txt
    ],
)
