# Chinese Word Segmentation

In this exercise you will build a simple Chinese word segmenter.  

## Introduction

Perhaps the most obvious feature of Chinese text is the lack of explicit word boundaries. Unlike European languages, Chinese text does not separate its words with spaces; readers are expected to recognise the words, so this separation is not necessary. Separation is only used between sentences and significant phrases.  

A Chinese sentence is formed by a consecutive string of words, such as:

> 中文句子由连续的一系列单词组成

Each word consists of one or more characters. The above sentence would be segmented as follows:  

<table border="0" width="80%" align="center">

<tbody>

<tr align="center">

<td>中文</td>

<td>句子</td>

<td>由</td>

<td>连续</td>

<td>的</td>

<td>一系列</td>

<td>单词</td>

<td>组成</td>

</tr>

<tr align="center">

<td>Chinese</td>

<td>sentence</td>

<td>cause/with</td>

<td>consecutive</td>

<td>(adjective marker)</td>

<td>a series of</td>

<td>word</td>

<td>formed</td>

</tr>

</tbody>

</table>

Text segmentation is the task of identifying the individual words in the text, and is a necessary starting point for most kinds of analysis of Chinese text, e.g. tagging, phrase analysis, entity recognition, translation. This task can be difficult because most characters may be individual words themselves, but could also be part of a longer multi-character word. Humans can differentiate the words quite easily, but it is not so simple for a machine.  

_If Chinese text is not displayed correctly in your web browser, it may be necessary to change the page's interpreted character encoding. For viewing Chinese text files in a text editor, it may be necessary to select a Chiniese font (e.g. "MS Mincho") for the characters to be correctly displayed._

### Greedy Matching

A simple approach to Chinese segmentation is to use a list of known words, and try to find matching sequences of characters in the text that appear in this list, with a preference for the longest match found. Statistics show that the majority of Chinese words are up to 5-characters long, so we can reduce our searching by limiting the word length to 5 characters.  

To segment a sentence using a list of known Chinese words:  

*   Start at the beginning of the sentence.
*   Find the longest sequence of (up to 5) consecutive characters that appears in the word list.
*   If a match is found consider that substring a word and move one character beyond the end of the matched string and search for a match again.
*   If none is found, assume a single-character word.
*   Continue matching until the end of the sentence.

For example, given the sentence: 中文句子由连续的一系列单词组成  
中文句子由, 中文句子, and 中文句 do not appear in our word list, but 中文 does, so that is our first word.  
Then we continue, checking for 句子由连续, 句子由连, and so on; we find 句子 as our next word.  
This is repeated until the end of the sentence, giving: 中文 / 句子 / 由 / 连续 / 的 / 一系列 / 单词 / 组成.

### Handling UTF-8 Files in Python

When Unicode text is written to a file, each character can not be stored as a single byte, and so they must be encoded in a special form. UTF-8 is one such encoding that stores characters in a variable number of bytes as necessary. Reading UTF-8 encoded text from files requires a decoding process to retrieve the original Unicode text.  
Our Chinese texts are encoded with UTF-8, so we must take care when reading the text from files, writing text to files, and displaying text on the screen.  

#### Reading from files:

```python
import codecs  

infile = "chinesetext.utf8"  
f = codecs.open(infile,mode='r',encoding="utf8")  

line = f.readline()   #'line' contains a line of Unicode text (decoded from UTF-8)
#...do something...

f.close()  
```

#### Writing to files:

```python
import codecs  
   
outfile = "chinesetext_seg.utf8"  
g = codecs.open(outfile,mode='w',encoding="utf8")  
  
#'chinese_text' contains a line of Chinese characters (Unicode) 
g.write(_chinese_text_)   #write text to file (encoded with UTF-8)
  
g.close()  
```

#### Printing to screen:

**#Note: this only works in terminals that support display of UTF-8 encoded characters.**  
**#An alternative is to redirect the output to a file and display that.**  

```python
import codecs  
  
infile = "chinesetext.utf8"  
f = codecs.open(infile,mode='r',encoding="utf8")  
  
for line in f:  
    print line.encode("utf8")  #encode a single line with UTF-8 
  
f.close()  
```

## Exercises

Build a Chinese word segmenter that reads the unsegmented text, segments it in to words using the supplied Chinese word list, and outputs the segmented text.  

Download the [unsegmented Chinese text](chinesetext.utf8) and [Chinese word list](chinesetrad_wordlist.utf8).  
The Chinese text contains one sentence per line, no numbers, and no punctuation. The Chinese word list contains one word per line.  

Your program should take two command-line arguments: (1) the file name of the word list, and (2) the name of the unsegmented text file; it should output one sentence per line, in the same order as the unsegmented text, with segmented words separated by spaces.

### Evaluation

Evaluate the performance of your segmenter on the [correctly segmented text](chinesetext_goldstandard.utf8) using the supplied [evaluation script](evalChinSeg.py).  

```bash
python evalChinSeg.py chinesetext_segmented.utf8 chinesetext_goldstandard.utf8
```

The evaluation program will compare each of your sentences (_chinesetext_segmented.utf8_) to the correct segmentation (_chinesetext_goldstandard.utf8_) and display the percentage of correctly segmented words.

### Other Resources

The Chinese texts for this assignment come from the Sinica Treebank corpus of traditional Chinese, which is included in NLTK. [This](generateChineseResources.py) is the python script we used to create the files used in this assignment.  

Further information on processing texts in Python using Unicode can be found in [Chapter 3.3](http://www.nltk.org/book/ch03.html#sec-unicode) of the NLTK book.
