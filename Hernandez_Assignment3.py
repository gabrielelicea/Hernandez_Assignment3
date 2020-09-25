import requests
import csv
import operator
import re


def listMerger(link):
    resp = requests.get(link)
    file = resp.text
    lines = file.splitlines()
    for line in lines:
        mergedList.append(line)


quit = False
while not quit:
    print("        Hernandez's CompanyList Data Analyzer: ")
    print("========================================================")
    print("1. Export to merged/sorted(by stock symbol) CSV file")
    print("2. Search by stock symbol")
    print("3. Display 15 companies with the highest Market Cap value")
    print("4. Exit")
    print("   --------------------------------")
    option = int(input("   Please choose one of the above: "))

    link1 = "https://raw.githubusercontent.com/gheniabla/datasets/master/companylist-1.csv"
    link2 = "https://raw.githubusercontent.com/gheniabla/datasets/master/companylist-2.csv"
    link3 = "https://raw.githubusercontent.com/gheniabla/datasets/master/companylist-3.csv"

    if option == 1:
        # categories = "Symbol Name LastSale MarketCap ADR TSO IPO year Sector	Industry Summary Quote"
        mergedList = []

        listMerger(link1)
        listMerger(link2)
        listMerger(link3)

        mergedList.sort()
        f = open("mergedCompanyList.csv", "w")
        f.writelines('\n'.join(mergedList))
        f.close()

    elif option == 2:
        # search for stock
        stockSearch = input("Enter the stock symbol you wish to search: ")
        with open('mergedCompanyList.csv', 'r') as f:
            for line in f:
                if stockSearch in line:
                    print(line)
                    break

    elif option == 3:
        reader = csv.reader(open("mergedCompanyList.csv"), re=',')
        for Symbol, Name, LastSale, MarketCap, ADR, TSO, IPOyear, Sector, Industry, SummaryQuote, in reader:
            sortedList = sorted(reader, key=operator.itemgetter(2), reverse=True)
            print(sortedList)
            # display 15 companies with highest market cap

    elif option == 4:
        quit = True
    else:
        raise Exception("Wrong Option")

