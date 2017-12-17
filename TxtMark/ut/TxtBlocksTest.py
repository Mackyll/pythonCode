import unittest,TxtMark.TxtBlocks,os


class TxtBlocksCase(unittest.TestCase):
    def test_blocks(self):
        f=open("block.txt","w")
        f.write("title\n\nthis ia blocks content\n\nthis is blocks content 2\n\n")
        f.close()

        block1=[]
        for block in TxtMark.TxtBlocks.blocks("block.txt"):
            block1.append(block)
        os.remove("block.txt")
        matchcase=["title","this ia blocks content","this is blocks content 2"]
        self.assertEqual(matchcase,block1)

