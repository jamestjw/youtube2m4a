import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='youtube2m4a',  
     version='0.1',
     scripts=['youtube2m4a.py'] ,
     author="James Tan",
     author_email="james_tan97@outlook.com",
     description="A wrapper on top of youtube-dl to download playlists of songs.",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/jamestjw/youtube2m4a",
     packages=setuptools.find_packages(),
     install_requires=[
        "bs4", "youtube-dl"
     ],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )