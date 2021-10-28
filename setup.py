import reflux
import setuptools

url = "https://github.com/frissyn/reflux"
# readme = open("README.md").read()
description = "Python package for creating IDE themes on Replit."

setuptools.setup(
    name="reflux",

    license="MIT",
    description=description,
    version=reflux.__version__,
    packages=setuptools.find_packages(),
    project_urls={
        "Source Code": url,
        "Pull Requests": url + "/pulls",
        "Issue Tracker": url + "/issues",
    },

    # long_description=readme,
    # long_description_content_type="text/markdown",

    include_package_data=True,
    python_requires=">=3.8.0",

    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development"
    ]
)