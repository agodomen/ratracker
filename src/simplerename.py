import os,random,string,shutil
import datetime 
path=".";
src="./data";
#path=raw_input("src path:");
directorys=os.listdir(src);
i=0;
def rename():
	
	for directory in directorys:
	    print "####",directory," is doing ####";
	    path=src+"/"+directory;
	    files=subfilesName(path)
	    i=0;
	    for f in files:
		print os.path.join(f),"...."
	    	if os.path.isfile(os.path.join(path,f))==True:
			i=i+1;
			name="{0:0{1}d}".format(i,4);			
			print f,"-->",name
			return name;


def getTimeName(directory):	
	    	i=datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')	
		name="{0}.png".format(i);
		print "##: .... ",name
		return name;

def subdirs(path):
    dl = [];
    for i in os.walk(path, False):
        for d in i[1]:
            dl.append(os.path.join(path, d))
    return dl

def subfiles(path):
    fl = [];
    for i in os.walk(path, False):
        for f in i[2]:
            fl.append(os.path.join(path, f))
    return fl

def subfilesName(path):
    fl = [];
    for i in os.walk(path, False):
        for f in i[2]:
            fl.append(f)
    return fl


def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0, length)]
    return str

def random_string(randomlength=8):
    a = list(string.ascii_letters)
    random.shuffle(a)
    return ''.join(a[:randomlength])
rename();
