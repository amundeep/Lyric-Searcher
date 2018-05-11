# Topical Song Suggestions

A system that allows you to discover new songs based on your interests in the songs lyrics and what the song is discussing, rather than the song’s genre.  So by looking for certain topics, you can find different songs that discuss that topic as well.  The following is a research report oriented around the use of this system.

Included in this repository is the .pdf file of the research report that goes into much further detail.  Below is instructions to run the script used to conduct the research.

## Getting Started

You will need Python 3 and MeTA/Metapy installed in order to run the testing program script on your machine.

### Installing

First you have to install Python using Homebrew or by downloading it off of the internet.  Below is an example of using Homebrew in order to install Python. 

```
brew install python
```

After checking to make sure Python is installed correctly, use the included pip/pip3 to install the Metapy software, which is what our script uses in order to process the text.

```
pip3 install metapy
```

To check that you have Metapy installed correctly, open a Terminal window and type

```
python3
>>> import metapy
>>> print(metapy.__version__)
0.2.10
```

If a version number prints then you're good to go!

## Running the tests

Once everything has been installed, open a Terminal window and "cd" into the directory where all the files are.  Then run:

```
python3 lda_script.py config.toml output 3
```

Which will run the testing script with 3 topics.  You can change this value at will.
At that point, the output-document.txt and output-topic.txt files hold the values of the topic model distribution for each song.  The key to what songs correspond to what index is available in the /lyrics/ directory under song-key.txt.

