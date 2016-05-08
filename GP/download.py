#coding:utf-8
import urllib
import requests
import threading
import Image
from bs4 import BeautifulSoup
import re
class download():
    def urlencode(self, words):
        #st = unicode(words, "utf-8")
        st = words.encode('gb2312')
        m = {'par':st,}
        s = urllib.urlencode(m)
        s = s.strip('par=')
        return s
    
    def get_linklist(self, url_words, page):
        url = 'http://www.netbian.com/e/sch/index.php?page='+str(page)+'&keyboard='+url_words 
        headers = {        
                   "Host":"www.netbian.com",
                   "User-Agent": "Mozilla/5.0(X11; Ubuntu; Linux x86_64; rv:31.0)Gecko/20100101 Firefox/31.0",
                   "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                   "Accept-Language":"zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3",
                   "Accept-Encoding":"gzip,deflate",
                   "Connection": "keep-alive",
        }
        web = requests.get(url,headers = headers)
	source = web.text
	linklist = re.findall(r"/desk/[0-9]{1,7}\.htm",source)
	newlist = list(set(linklist))
        return newlist    
    
    def saveImage(self, imgUrl,imgName ="default.jpg" ):
	headers = {
                   "Host":"img.netbian.com",
                   "User-Agent": "Mozilla/5.0(X11; Ubuntu; Linux x86_64; rv:31.0)Gecko/20100101 Firefox/31.0",
                   "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                   "Accept-Language":"en-US,en;q=0.5",
                   "Accept-Encoding":"gzip,deflate",
                   "Connection": "keep-alive",
        }
        response = requests.get(imgUrl, headers = headers, stream = True)
        image = response.content
        DstDir="/home/allen/GP/src/"
        try:
            with open(DstDir+imgName ,"wb") as jpg:
                jpg.write( image)    
                return
        except IOError:
            print("IO Error\n")
            return
        finally:
            jpg.close
	    im = Image.open("/home/allen/GP/src/"+imgName)
            out = im.resize((300,150))
            str_list = list(imgName)
            str_list.pop()
            str_list.pop()
            str_list.pop()
            str_list.pop()
            new = "".join(str_list)
	    print new
            out.save("/home/allen/GP/src/"+new+".png")
 
    def downImageViaMutiThread(self, linklist ):
	headers = {
                   "Host":"www.netbian.com",
                   "User-Agent": "Mozilla/5.0(X11; Ubuntu; Linux x86_64; rv:31.0)Gecko/20100101 Firefox/31.0",
                   "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                   "Accept-Language":"en-US,en;q=0.5",
                   "Accept-Encoding":"gzip,deflate",
                   "Connection": "keep-alive",
        }

        task_threads=[]  #存储线程
        count = 0
        for link in linklist:
	    web = requests.get("http://www.netbian.com"+link,headers = headers)
	    source = web.text
	    link = re.findall(r"img src=\"http:[\.\/a-z0-9]*\.jpg",source)
	    des_link = link[0].lstrip('img src=\"')
	    print "link:",des_link
            filename = "r" + str(count/6 + 1) + str(count%6 + 1) + ".jpg"
            t = threading.Thread(target=self.saveImage,args=(des_link,filename))
            count = count+1
            task_threads.append(t)
        for task in task_threads:
            task.start()
        for task in task_threads:
            task.join() 

    def getpng(self): 
	for i in range(3):
		for j in range(6):
			im = Image.open("/home/allen/GP/src/r"+str(i+1)+str(j+1)+".jpg")
			out = im.resize((300,150))
			out.save("/home/allen/GP/src/r"+str(i+1)+str(j+1)+".png")
if __name__ == "__main__":
    dl = download()
    a = dl.urlencode('a')
    b = dl.get_linklist(a, 0)
    dl.downImageViaMutiThread(b)
#    dl.getpng()
#    print b
