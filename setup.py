from setuptools import setup, find_packages

setup(
    name="cherry_template_app",
    version="1.0.0",
    author="Abhishek Yadav",
    author_email="abhishek.yadav@cubexo.io",
    description="A Custom Django admin template with CSS styling.",
    long_description_content_type="text/markdown",
    url="https://github.com/abhishek-cubexo1223/cherry_template.git",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Framework :: Django",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "django>=3.2",
    ],
    python_requires=">=3.6",
)
