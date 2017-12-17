import TxtMark.TxtBlocks

def mark(src,dest):
    html="<html><head><title>...</title><body>"
    first=True
    for block in TxtMark.TxtBlocks.blocks(src):
        if first:
            html+="<h1>"+block+"</h1>"
            first=False
        else:
            html+="<p>"+block+"</p>"
    html+="</body></html>"
    f=open(dest,"w")
    f.write(html)
    f.close()

mark("/Users/yankebiao/Documents/workspace/python/TxtMark/datingTestSet2.txt",
     "/Users/yankebiao/Documents/workspace/python/TxtMark/datingTestSet2.html")