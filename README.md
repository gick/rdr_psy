# rdr_psy
Scrapper for the rdr part of pschoactif.org
# Requirement
Python 2.7
Scrapy (python lib)
# Usage
clone dir

From /rdrpsy/rdrpsy :

scrapy crawl rdr -o output.json

This should give you a formatted output containing information about rdr 
from psychoactif.org

The list of postcode is currently stored in villex.txt file, I chose to put the 500 postcode associated with the largest population, for this I used http://sql.sh/736-base-donnees-villes-francaises

