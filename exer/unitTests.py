import unittest
from fileWriter import *
from exws import *

class UnitTests(unittest.TestCase):
    def testWriteToFileTrue(self):
        self.assertEqual(writeToFile("Leia Organa", "Bespin"), "1")

    def testGetUploadTrue(self):
        upload = UploadRebel()
        self.assertEqual(upload.GET("Luke Skywalker", "Tatooine"), "1")

    def testGetUploadFalse(self):
        upload = UploadRebel()
        self.assertEqual(upload.GET("Luke Skywalker", ""), ("FIELDERROR","Please fill the two fields" ))

if __name__ == '__main__':
    unittest.main()