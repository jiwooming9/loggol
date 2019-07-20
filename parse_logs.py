import time, os, re
from datetime import datetime

# Regex de tim cac dong log va loc truong du lieu
error_regex = re.compile(r"#")
regexp = re.compile(r'(?P<date>\d{4}-\d{2}-\d{2}) ' +
                    '(?P<time>\d{2}:\d{2}:\d{2}) ' +
                    '(?P<sourceip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}) ' +
                    '(?P<csmethod>[A-Z]+) ' +
                    '(?P<csuristem>[^ ]+) ' +
                    '(?P<csuriquery>[^ ]+) ' +
                    '(?P<sport>\d{0,5}) ' +
                    '(?P<csusername>[^ ]+) ' +
                    '(?P<cip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}) ' +
                    '(?P<csUserAgent>[^ ]+) ' +
                    '(?P<csReferer>[^ ]+) ' +
                    '(?P<csstatus>[^ ]+) ' +
                    '(?P<cssubstatus>[^ ]+) ' +
                    '(?P<cswin32status>[^ ]+) ' +
                    '(?P<timetaken>[^ ]+)')

# File output chua log hop le
output_filename = os.path.normpath("script-log.txt")

# Ham cap nhat du lieu moi cua file log giong tail -f cua python
def follow(thefile):
    thefile.seek(0,2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line


logfile = open("C:\\inetpub\\logs\\LogFiles\\W3SVC1\\u_ex190703.log")
loglines = follow(logfile)
counter = 0

for line in loglines:
    m = regexp.match(line)
    if (error_regex.search(line)):
        #Phan tach phien lam viec theo tuy chinh trong IIS log luu vao file output
        counter += 1
        sttime = datetime.now().strftime('%Y%m%d_%H:%M:%S - ')
        out_file=open(output_filename, "a")
        out_file.write(sttime + line)
        out_file.close()
    else:
        #In cac dong log ra file output
        out_file = open(output_filename, "a")
        out_file.write(line)
        counter = 0
        out_file.close()
    if not m:
        continue
    #In log ra console, co phan tach theo tung truong
    print(
        'Date: %s, Time: %s, Source IP: %s, CS Method: %s, CS Uri Stem: %s, CS Uri Query: %s, Source Port: %s, CS Username: %s, C IP: %s, CS UserAgent: %s, CS Referer: %s, CS Status: %s, CS Substatus: %s, CS Win32 Status: %s, Timetaken: %s' % (
        m.group('date'),
        m.group('time'),
        m.group('sourceip'),
        m.group('csmethod'),
        m.group('csuristem'),
        m.group('csuriquery'),
        m.group('sport'),
        m.group('csusername'),
        m.group('cip'),
        m.group('csUserAgent'),
        m.group('csReferer'),
        m.group('csstatus'),
        m.group('cssubstatus'),
        m.group('cswin32status'),
        m.group('timetaken')))

