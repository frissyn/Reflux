import reflux
import setuptools

readme = open("README.md").read()
url = "https://github.com/frissyn/Reflux"

setuptools.setup(
    name="reflux",
    license="MIT",
    author="frissyn",
    description=reflux.__doc__,
    version=reflux.__version__,

    url=url,
    project_urls={
        "Source Code": url,
        "Pull Requests": url + "/pulls",
        "Issue Tracker": url + "/issues",
        "Documentation": url + "/tree/master/docs"
    },

    long_description=readme,
    long_description_content_type="text/markdown",

    python_requires=">=3.7.0",
    install_requires=["pyyaml"],

    zip_safe=False,
    packages=["reflux"],
    include_package_data=True,

    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development"
    ]
)