import unittest, TxtMark.TxtMarker, os


class TxtMarkerCase(unittest.TestCase):
    def test_maker_case(self):
        f = open("srcFile.txt", "w")
        f.write("title\n\nthis is a content\n\nthis a come after content\n\n")
        f.close()
        matchcase1 = "<html><head><title>...</title><body>" \
                     "<h1>title</h1><p>this is a content</p><p>this a come after content</p></body></html>"
        TxtMark.TxtMarker.mark("srcFile.txt", "destFile.txt")
        f = open("destFile.txt", "r")
        matchcase2 = f.read()
        os.remove("srcFile.txt")
        os.remove("destFile.txt")
        self.assertEqual(matchcase1,matchcase2,"test")
