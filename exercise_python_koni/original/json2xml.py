import json
import dicttoxml
from bs4 import BeautifulSoup

"""
○使用外部パッケージ
    poetry add BeautifulSoup4
    poetry add lxml
○参考
    jsonからxmlについて
        https://qiita.com/kkdmgs110/items/9317057facb60764ed74
    BeautifulSoupやパーサについて
        https://qiita.com/PND/items/06e1053eeed69ec4f418
        https://lets-hack.tech/programming/languages/python/beautifulsoup-xml/
○内容
    指定したjsonファイルを読み込み、xmlに変換する。その後パース(見やすく)し、ファイル出力する。
    ここでは「jsonfile.json」を読み込み、「xmlfile.xml」を出力している。。

"""

def json2xml():
    translatedjsonFile = jsontodictFile(readjson())
    translatedxmlFile = dicttoxmlFile(translatedjsonFile)
    writexml(soupxmlfile(translatedxmlFile))
    
    
def readjson():
    TargetFile = open('jsonfile.json','r')
    return TargetFile


def writexml(writeFile):
    with open('xmlfile.xml', 'wt') as xmlFile:
        xmlFile.write(writeFile)


def soupxmlfile(soupfile):
    soup = BeautifulSoup(soupfile, "lxml")
    return soup.prettify()


def jsontodictFile(Targetfile):
    translateddictFile = json.load(Targetfile)
    return translateddictFile


def dicttoxmlFile(Targetfile):
    translatedxmlFile = dicttoxml.dicttoxml(Targetfile)
    return translatedxmlFile


if __name__=='__main__':
    json2xml()
