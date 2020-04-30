from distutils.core import setup, Extension

pyClientLib_module = Extension(
    'pydpclient',
    sources=['pyClientLib.c'],
    include_dirs=['client-lib-cpp'],
    libraries=[
        "ClientLib",
        "stdc++",
    ],
    library_dirs=["client-lib-cpp/lib"],
)

setup(
    name='dp_client',
    author="Andrey Bibea",
    author_email="bibea@nanosemantics.ai",
    version='1.0',
    ext_modules=[
        pyClientLib_module,
    ],
    packages=["dp_client"],
)
