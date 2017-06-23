from lib import *
import sys
if __name__ == '__main__':
    print("正在分析页面")
    webpage = GetHtml(sys.argv[1:][0])
    Links = GetUrlList(webpage)
    print("此网页上共有%d条链接记录,已生成目录文件。" % len(Links))
    fileName = sys.argv[1:][0].split(".")[1]     
    id = 1
    for Link in Links:
        print(Link)
        #webpagecache = GetHtml(Link)
        #webpage = WebPagePrecess(webpagecache)
        #print("已经处理了%d个" % id)
        #id += 1
        #WriteFile(webpage, fileName + ".txt")
   # input("共%d个页面，全部处理完成，按回车键退出。" % len(Links))
