import json
import dicttoxml
from bs4 import BeautifulSoup
from pprint import pprint

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
    ここでは「jsonfile.json」を読み込み、「xmlfile.xml」を出力している。

"""

def json2xml(): 
    translatedjsonFile = jsontodictFile(readjson())
    translatedxmlFile = dicttoxmlFile(translatedjsonFile)
    writexml(shapingxmlfile(translatedxmlFile))
    # print("jsonからxmlを作成完了")


def readjson():
    TargetFile = open('jsonfile.json','r')
    return TargetFile


def writexml(writeFile):
    # print("書き込み中")
    with open('xmlfile.xml', 'wt') as xmlFile:
        xmlFile.write(writeFile)


def shapingxmlfile(xmlfile):
    # print("xmlFileを整形中")
    shapingfile = BeautifulSoup(xmlfile, "lxml")
    return shapingfile.prettify()


def jsontodictFile(Targetfile):
    # print("jsonから辞書に変換中")
    translateddictFile = json.load(Targetfile)
    return translateddictFile


def dicttoxmlFile(Targetfile):
    # print("辞書からxmlに変換中")
    translatedxmlFile = dicttoxml.dicttoxml(Targetfile)
    # print(translatedxmlFile)
    return translatedxmlFile


if __name__=='__main__':
    json2xml()
