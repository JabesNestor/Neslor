from setuptools import setup, find_packages

setup(
    name="Neslor", 
    version="0.1.0",       
    description="Librería de paletas de colores personalizadas",
    author="Jabes Frías",
    author_email="Jabesnestor@gmail.com",
    url="https://github.com/JabesNestor/Neslor",
    packages=find_packages(),  
    install_requires=["matplotlib"],  
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
