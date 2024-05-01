# About
This repository aims to collect and aggregate JEL (Journal of Economic Literature) Classification Codes. According to the American Economic Association's website, JEL "... is a standard method of classifying scholarly literature in the field of economics". For further information, click [here](https://www.aeaweb.org/jel/guide/jel.php).

# Use case
Say you are an early career research economist. You have written an academic paper and want to submit it to a journal. However, you are not sure which journal that might fit to your research. Surely you don't your paper being rejected just because the journal that you're targeting doesn't publish or has stopped publishing papers with similar topic(s) of yours. This repository hopefully helps you navigate those as you can track the trends of JEL Classification Codes by each journal and year.

You can see the complete list of journals on the `/data/` directory.

Please note that though I am trying to provide as much journals as possible, this repository is by no means comprehensive. So I apologize in advance!

# Guide
If you want to run the code, make sure you have installed all the required libraries (see `requirements.txt`). Following is a code example that you can run yourself:

```python
# make sure you are in the /jel directory

import jel

# assign variables
# for example, let's use Springer's Economic Theory (https://link.springer.com/journal/199)
journal = "199"
journal_long = "Economic Theory"
path = "../data/economic-theory"

# assign a class
springer = jel.Springer()

# scrape the website
issue = springer.get_issue(journal)
for i in issue:
    article = springer.get_article(i)
    springer.save_data(i, article, path, journal, journal_long)

# if successful, data will be saved on the /data/economic-theory/ directory
# similarly for other journals
```

# Special note
This repository is inspired by a book titled [Doing Economics: What You Should Have Learned in Grad School—But Didn't](https://mitpress.mit.edu/9780262543552/doing-economics/) by [Marc F. Bellemare](https://marcfbellemare.com/wordpress/).
