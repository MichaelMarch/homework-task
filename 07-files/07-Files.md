# 07*Files

`1`. Search the Internet for a definition of a computer file. List types of files you know.  
> Computer file is a named resource used for storing data.  
> File types that I know:  
> * Image types: **png**, **jpg**, **jpeg**, **tiff**, **gif**, **svg**
> * Text types: **txt**, **md**, **ini**, **html**, **xml**, **py**, **gd**, **java** 
> * Video types: **mp4**, **wmv**, **mov**, **avi**, **flv**
> * Audio types: **m4a**, **mp3**, **wav**, **opus**
> * Binary types:
>     * Executable binaries: **exe**, ***none***, **bin**
>     * Data: **scn**, **bin**
>     * Objects: **dll**, **o**, **lib**, **so**, **obj**, **bin**
>     * Documents: **doc**, **pdf**

`6`. Then create regular expressions they indicate in the text:
1. All words "Poland"
    > <font color="green">**Poland('s)\***</font>
2. Country names (Poland, Germany and France)
    > <font color="green">**Poland|Germany|France**</font>
3. Punctuation marks (dots and commas)
    > <font color="green">**\\.|,**</font>
4. Numbers representing a year (four-digit numbers)
    > <font color="green">**\d{4}**</font>
5. Capital letters
    > <font color="green">**[A-Z]**</font>
6. Vowels (assuming that `y` is a vowel for simplicity)
    > <font color="green">**a|e|i|o|u|y**</font>
7. Words with at least five letters.
    > <font color="green">**\b\w{5,}\b**</font>
8. Words starting with capital letters
    > <font color="green">**[A-Z]\w+**</font>