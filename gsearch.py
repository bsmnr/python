#!/usr/bin/env python3

################################################################################################################################################################################
# Information: Simple Google Search Python Script for command line, that accepts user input as an argument for the search. This can be a word or a phrase.
#
# Notes: I was not expecting for the actual python script to be counted as an argument using sys library. I will research this at a later date to figure out how to simplify it
#        hopefully understand why it counts as an argument. By default googlesearch is supposed to return 10 results. I continue to only return 8. 
# Update: As I researched the sys library it seems that the python script will always be counted as an argument and indexed at 0.
#
# Syntax: gsearch.py tacobell                                 
#		  gsearch.py tacobell rules! McDonalds drools!                                                                                                  
#################################################################################################################################################################################

import sys
from googlesearch import search

query = str(sys.argv)
		
for url in search(query):
	print(url)