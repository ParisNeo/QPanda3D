import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='QPanda3D',  
     version='0.2',
     author="Saifeddine ALOUI",
     author_email="aloui.saifeddine@gmail.com",
     description="A binding to use Panda3D as a PyQt5 widget",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/ParisNeo/QPanda3D",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
         "Operating System :: OS Independent",
     ],
 )