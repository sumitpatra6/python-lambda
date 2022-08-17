from setuptools import setup, find_packages

packages = find_packages()



setup(
    name = "lambda tutorial",
    version="1.0",
    description="Python lambda project",
    author="Sumit Patra",
    author_email="sumitpatra6@gmail.com",
    url="https://github.com/sumitpatra6/python-lambda",
    install_requires=["requests", "boto3"],
    packages=packages,
    include_package_data=True
)