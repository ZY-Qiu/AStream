import re
import datetime
import csv

def main():
    print("Running\n")
    filename = r"C:\Users\QiuGeGe\Desktop\c2.log"
    dfname = r"C:\Users\QiuGeGe\Desktop\trunc_c2.csv"

    with open(filename) as f:
        content = f.readline()
        start_time = datetime.datetime.strptime(content[0:19], "%Y-%m-%d %H:%M:%S")
        shift = float(content[20:23]) / 1000
        start_time += datetime.timedelta(seconds=shift)
        with open(dfname, "w", newline="") as clean:
            pass
        with open(dfname, "a", newline="") as handle:
            result_writer = csv.writer(handle, delimiter=",")
            result_writer.writerow("time,Download Rate,next_bitrate".split(","))

        datas = f.readlines()
        for data in datas:
            if(re.search("Download Rate", data) != None):
                t = datetime.datetime.strptime(data[0:19], "%Y-%m-%d %H:%M:%S")
                shift = float(data[20:23]) / 1000
                t += datetime.timedelta(seconds=shift)

                l = [(t - start_time).seconds]
                l += re.findall(r"\d+\.\d+", data[72:])
                with open(dfname, "a", newline="") as handle:
                    result_writer = csv.writer(handle, delimiter=",")
                    result_writer.writerow(l)
    
    with open(dfname) as f:
        reader = csv.reader(f, delimiter = ',')



main()