import pandas as pd
import csv

CSVfilename = "test.csv"
TXTfilename = "test.txt"

#将txt妆化为csv
def TXTtoCSV(Orgfilename):
    with  open(Orgfilename, "r", encoding='utf-8') as f1 ,open(CSVfilename,'w', encoding='utf-8') as f2:
        data = f1.readlines()
        for line in data:
            triple = line.strip().split(' ')
            writer = csv.writer(f2)
            writer.writerow((triple[0],triple[1],triple[2]))
    f1.close()
    f2.close()

#将csv转化为txt
def CSVtoTXT(Orgfilename):
    data = pd.read_csv(Orgfilename,skiprows=1 ,nrows =10,encoding='utf-8') #skiprows跳过多少,nrows提取多少 ,
    with open(TXTfilename,'w', encoding='utf-8') as f:
        for line in data.values:
            f.write((str(line[0])+' '+str(line[1])+' '+str(line[2])+'\n'))
    f.close()

##将csv删除重复行
def CSVset(Orgfilename):
    data = pd.read_csv(Orgfilename,encoding='utf-8')
    newDF = data.drop_duplicates();

    with open('triple.csv','w', encoding='utf-8') as f:
        writer=csv.writer(f)
        i = 0
        for line in newDF.values:
            writer.writerow((str(line[0]), str(line[1]), str(line[2])))
            i = i + 1
        print(i)
    f.close()


#TXTtoCSV("AfterTriple.txt")
CSVtoTXT("test.csv")

