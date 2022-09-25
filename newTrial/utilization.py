import re
import datetime
import csv

def main():
    print("Running\n")
    filename = r"C:\Users\QiuGeGe\Desktop\iftop.log"
    dfname = r"C:\Users\QiuGeGe\Desktop\iftop_trunc.log"
    ans = 0
    cnt = 0

    with open(filename) as f:
        with open(dfname, "w", newline="") as clean:
            pass
        datas = f.readlines()
        for data in datas:
            if(re.search("Total send rate", data) != None):
                # l = re.findall(r"\d+\.\d+", data[50:])
                # print(l[0])
                # ans += float(l[0])
                # cnt += 1
                # print(data[53:60])
                s = data[53:60]
                if(s[-3:-1] == "Mb"):
                    ans += float(s[0:4])
                else:
                    ans += float(s[0:4])/1000
                cnt += 1
                with open(dfname, "a", newline="") as handle:
                    handle.write(data)
    print(ans / cnt)
    
main()