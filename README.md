## Thamizhi-Preprocessor  

This has a set of functions written in python using which you can validate whether a word is a Tamil word according to a Tamil classical grammar text called Nannool. This will also show whether a given word is a one letter word (ஓரெழுத்தொருமொழி) 

Further, this also can be used to Unicode normalise Tamil content in a given file.
- Unicode Unicode Normalizer

# How to use this script

## To check word validity
```
python3.8 thamizhi-preprocessor.py -validate word-to-be-validated
For instance,
python3.8 thamizhi-preprocessor.py -validate சங்கம்
```
Based on the validation you will see different outputs.


## To Normalise a text file
Because of an input method or application, orthographically equalent words may be save with different Unicode points. 
For insance, take the following words: கொக்கு and கொக்கு
Both looks the same, however, they are store in different ways as the following sequence. 
க ெ ா க ் க ு and க ொ க ் க ு
Therefore, it is important to normalise to one acceptable for before do any processing. This script does it, and this is made spcifically for Tamil.

```
python3.8 thamizhi-preprocessor.py -normalise file-to-be-normalised
For instance,
python3.8 thamizhi-preprocessor.py -normalise sample-text
```
This will create a new normalised file: normalised-sample-text

*How can I improve this, write to me please!*
