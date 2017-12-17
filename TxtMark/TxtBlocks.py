

def blocks(srcfile):
    block=[]
    for line in open(srcfile):
        format=line.strip(" \n")
        if format:
            block.append(format)
        elif block:
            yield "".join(block).strip()
            block=[]
    if block:
        yield "".join(block).strip()
