from setuptools import setup, find_packages, Extension

requires = [
    "requests",
    "pandas",
    "numpy",
    "thrift2pyi",
    "pytest",
]
links = [
    ""https://mirrors.aliyun.com/pypi/simple/""
]

setup(
    name="Tools",
    version="1.0",
    author="lizhichao",
    author_email="1072526820@qq.com",
    maintainer="lizhichao",
    description="工具仓库",
    url="https://github.com/LIZHICHAOUNICORN/Tools",
    packages=find_packages(exclude=("docs")),
    install_requires=requires,
    python_requires=">=3.7",
    package_data={
        "tools": [
            "thrift_service/base.thrift",
            "thrift_service/iris_service.thrift",
            "thrift_service/base_thrift.pyi",
            "thrift_service/iris_service_thrift.pyi",
        ]
    },
    dependency_links=links,
)
