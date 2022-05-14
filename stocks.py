#!/usr/bin/env python3

########################################################################################################################################################################################
# Simple Python Script to look up basic data of a stock. Uses Yahoo Finance to pull data. Will be looking into PANDAS, NUMPY, and MATPLOTLIB to enhance this basic script in the future.
# Syntax: stocks.py <option> <ticker symbol>
########################################################################################################################################################################################

import sys
import getopt
import yfinance as yf

optlist, args = getopt.getopt(sys.argv[1:], "dsbe", ['dividends', 'splits', 'balance sheet', 'earnings'])

stock = yf.Ticker(sys.argv[2])

for option, argument in optlist:
	if option == "-d":
		print(stock.dividends)
	elif option in ('-s', "--splits"):
		print(stock.splits)
	elif option in ('-b', "--balance"):
		print(stock.balance_sheet)
	elif option in ('-e', "--earnings"):
		print(stock.earnings)
	else:
		print("Invalid Option. Please try again!")

# Looking at finding a way to make the stock info print nicely. Possibly prep it for easier referencing in future use. 
# info = str(stock.info).split(", ")
# print(stock.actions)

#for data in info:
#	print(data)