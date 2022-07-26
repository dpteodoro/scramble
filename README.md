# SCRAMBLED WORDS READER

Based on Google coding challenge.

## Premise
The human brain can still read misspelled words without much effort as long as the
misspelled word has the same beginning and ending letters as the original word.
This program tries to mimic the behavior of the human brain when it comes to reading.

## Solution
The solution is based on the Analysis section of the Scramble coding challenge.
This only applies to small datasets.

## Input
1. dictionary.txt - file containing words. Not necessarily valid English words, but must consist of the 26 lowercase English alphabet only.
2. input.txt - file containing long words (test case) against which words from the dictionary will be matched

## Output
Output will be test case number along with the number of matching dictionary words.

If dictionary.txt contains
```
axpaj
apxaj
dnrbt
pjxdn
abd
```

and input.txt contains
```
aapxjdnrbtvldptfzbbdbbzxtndrvjblnzjfpvhdhhpxjdnrbt
aapxjdnrbyvldptfzbbdbbzxtndrvjblnzjfpvhdhhpxjdnrbl
```

Then, output will be
```
Case #1: 4
Case #2: 3
```

## Running
### Via command line assuming python is installed.
It would be nice if there is a virtual env using python 3.9. In the scramble project directory, do

```
python scramble/src/main.py
```

### Via docker
#### Building
```
docker build -t reader .
```
where reader is an arbitrary image name.

#### Running
```
docker run reader
```

or if we want to mount our own test case
```
docker run -v /path/to/host/test_data_dir:/app/scramble/data reader
```