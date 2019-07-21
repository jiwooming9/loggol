import os, io


def parse_file(file_in, file_out):
    fin = open(file_in)
    fout = io.open(file_out, "w", encoding="utf-8")
    lines = fin.readlines()
    res = []
    for i in range(len(lines)):
        d = dict()
        line = lines[i].strip()
        if line.startswith("GET"):
            d['Method'] = line.split(" ")[0]
            d['URL'] = line.split(" ")[1].split('?')[0]
            d['Protocol'] = line.split(" ")[2]
            if len(line.split(" ")[1].split('?')) < 2:
                d['Payload'] = "null"
            else:
                d['Payload'] = line.split(" ")[1].split('?')[1]
            d['UserAgent'] = lines[i + 1].strip().split(": ")[1]
            d['Pragma'] = lines[i + 2].strip().split(": ")[1]
            d['CacheControl'] = lines[i + 3].strip().split(": ")[1]
            d['Accept'] = lines[i + 4].strip().split(": ")[1]
            d['AcceptEncoding'] = lines[i + 5].strip().split(": ")[1]
            d['AcceptCharset'] = lines[i + 6].strip().split(": ")[1]
            d['AcceptLanguage'] = lines[i + 7].strip().split(": ")[1]
            d['Host'] = lines[i + 8].strip().split(": ")[1]
            d['Cookie'] = lines[i + 9].strip().split(": ")[1]
            d['Connection'] = lines[i + 10].strip().split(": ")[1]
            d['ContentType'] = "null"
            d['ContentLength'] = "null"
            res.append(d)
        elif line.startswith("POST") or line.startswith("PUT"):
            d['Method'] = line.split(" ")[0]
            d['URL'] = line.split(" ")[1].split('?')[0]
            d['Protocol'] = line.split(" ")[2]
            j = 1
            while True:
                if lines[i + j].startswith("Content-Length"):
                    break
                j += 1
            j += 1
            d['Payload'] = lines[i + j + 1].strip()
            d['UserAgent'] = lines[i + 1].strip().split(": ")[1]
            d['Pragma'] = lines[i + 2].strip().split(": ")[1]
            d['CacheControl'] = lines[i + 3].strip().split(": ")[1]
            d['Accept'] = lines[i + 4].strip().split(":")[1]
            d['AcceptEncoding'] = lines[i + 5].strip().split(": ")[1]
            d['AcceptCharset'] = lines[i + 6].strip().split(": ")[1]
            d['AcceptLanguage'] = lines[i + 7].strip().split(": ")[1]
            d['Host'] = lines[i + 8].strip().split(": ")[1]
            d['Cookie'] = lines[i + 9].strip().split(": ")[1]
            d['Connection'] = lines[i + 11].strip().split(": ")[1]
            d['ContentType'] = lines[i + 10].strip().split(": ")[1]
            d['ContentLength'] = lines[i + 12].strip().split(": ")[1]
            res.append(d)
    for star in res:
        fout.writelines(str(star) + "\n")
    print("Parse", len(res), "requests")
    fout.close()
    fin.close()


parse_file('logtest\\normalTrafficTest.txt', 'logoutput\\CSIC NormalTrafficTestOutput.txt')
parse_file('logtest\\anomalousTrafficTest.txt', 'logoutput\\CSIC AnomalousTrafficTestOutput.txt')
