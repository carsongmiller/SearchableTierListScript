# Wingsplain Make-Searchable Script
A simple python script to replace all bird names in the [Wingsplain](https://wingsplain.com/wingspan-bird-card-tier-list/) tier list with links to their corresponding page on [WingSearch](https://navarog.github.io/wingsearch/)

## How to use
1. Go to [WingSearch](https://navarog.github.io/wingsearch/) and keep scrolling down in order to load all birds
2. Right click and save as Webpage Complete (in Chrome)
3. Supply a file containing the Wingsplain html (I did this by saving the web page, but you may supply it in a different format)
4. Put both of these html files in the same directory as the script
5. Replace the two strings `wingsearchHTMLFileName` and `tierListHTMLFileName` in the script (makeSearchable.py) with your html files' names
6. Run the script.  The resulting html file will be called "madeSearchable.html"

## Notes
- There is a large section of code which corrects for all spelling differences between Wingsplain and WindSearch (they're mostly hyphenations and diacritics, with a couple potential just spelling mistakes on one sight or the other).
 - I made it so that all spelling on Wingsplain remained exactly as it was
- This program supports the core set, swift start pack, and europe, oceania, and asia expansions
 - If used in the future with future expansions, more spelling-mismatch cases would likely need to be added
 - The program searches the wingsearch code using a regex, so as long as they don't change the format of their html code, it should still find birds from new expansions