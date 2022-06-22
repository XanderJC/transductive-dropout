import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="TD",
    version="1.0.0",
    author="Alex J. Chan",
    author_email="ajc340@cam.ac.uk",
    description="Unlabelled Data Improves Bayesian Uncertainty Calibration under Covariate Shift.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/XanderJC/transductive-dropout",
    packages=setuptools.find_packages(),
    install_requires=[
        "autograd==1.3",
        "matplotlib==3.1.1",
        "numpy==1.22.0",
        "tqdm==4.36.1",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
