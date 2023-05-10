import setuptools

setuptools.setup(
    name="typeevalpy_external_module",
    version="1.2",
    description=(
        "External module for PyCG micro-benchmark with support for type inference"
    ),
    author="",
    author_email="",
    license="GPL-3.0",
    packages=setuptools.find_packages(),
    zip_safe=False,
)

# pip install --upgrade typeevalpy_external_module
