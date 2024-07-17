import os
from setuptools import setup, find_packages

from torch.utils import cpp_extension

os.environ["CC"] = "g++"
os.environ["CXX"] = "g++"

common_setup_kwargs = {
    "version": "0.0.1.dev0",
    "name": "hgemm_torchlib",
    "author": "fxmarty",
    "description": "cublas hgemm.",
    "keywords": ["half"],
    "platforms": ["linux"],
    "classifiers": [
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: C++",
    ]
}

requirements = [
    "torch",
]

extensions = [
    cpp_extension.CppExtension(
        name="mycppops",
        sources=["sinop_ext/torch_ext.cpp"]
    )
]

additional_setup_kwargs = {
    "ext_modules": extensions,
    "cmdclass": {'build_ext': cpp_extension.BuildExtension}
}
common_setup_kwargs.update(additional_setup_kwargs)
setup(
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.8.0",
    **common_setup_kwargs
)
