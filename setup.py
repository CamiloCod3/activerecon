from setuptools import setup, find_packages

setup(
    name="activerecon",           # Paketnamnet, används vid pip install
    version="0.1.0",              # Versionsnummer, öka vid nya releaser
    packages=find_packages(),      # Letar automatiskt igenom activerecon/-mappen efter moduler

    # Ange beroenden här:
    install_requires=[
        "requests",
        "paramiko",
        "rich",
        "dnspython",
        "xmltodict",
        "pyyaml"
    ],

    # Skapar ett konsol-kommando 'activerecon' som kör main()-funktionen i t.ex. activerecon/main.py
    entry_points={
        "console_scripts": [
            "activerecon=activerecon.main:main"
            # Om din fil heter activerecon.py i stället för main.py:
            # "activerecon=activerecon.activerecon:main"
        ]
    },

    # Se till att datafiler (som config.yaml) följer med om du vill distribuera dem
    include_package_data=True,

    # Metainfo om paketet
    description="Active Recon: An automated reconnaissance tool",
    author="Ditt Namn",
    author_email="dinmail@example.com",
    url="https://github.com/dinGit/ActiveRecon",
    license="MIT",

    # Klassificeringar (frivilligt men bra vid publicering på PyPI)
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    # Vilka Python-versioner som stöds
    python_requires='>=3.6',
)
