import requests
import csv
import operator

quit = False
while quit != True:
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
        resp1 = requests.get(link1)
        file1 = resp1.text
        lines1 = file1.splitlines()
        for line in lines1:
            mergedList.append(line)

        resp2 = requests.get(link2)
        file2 = resp2.text
        lines2 = file2.splitlines()
        for line in lines2:
            mergedList.append(line)

        resp3 = requests.get(link3)
        file3 = resp3.text
        lines3 = file3.splitlines()
        for line in lines3:
            mergedList.append(line)
            mergedList.sort()

        f = open("mergedCompanyList.csv", "w")
        f.writelines('\n'.join(mergedList))
        f.close()

    elif option == 2:
        # search for stock
        f1 = open('mergedCompanyList.csv', 'r')
        f1.readline()
        # f2 = sorted(f1,key=operator.itemgetter(5),reverse=True)
        # csv1 = csv.reader(f1, delimiter=',')
        # sort = sorted(csv1, key=operator.itemgetter(2))
        # for eachline in f2:
        #     print(eachline)
    # elif option == 3:
    # display 15 companies with highest market cap
    elif option == 4:
        quit = True
    else:
        raise Exception("Wrong Option")
