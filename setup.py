from setuptools import setup, find_packages

INSTALL_REQUIRES = [
    "pyyaml",
    "fastapi",
    "coloredLogs",
    "sqlalchemy",
    "python-dotenv",
    "dotenv",
    "fastapi_sqlalchemy",
]
_EXTRAS_REQUIRES = {"docs": ["sphinx", "furo"], "tests": ["pytest"]}

setup(
    name="zaatot",
    version="0.1.0",
    author="z_sarrar",
    install_requires=INSTALL_REQUIRES,
    extras_require=_EXTRAS_REQUIRES,
    email="zouhirsarrar@gmail.com",
    packages=find_packages(),
)
