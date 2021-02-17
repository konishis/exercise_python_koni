import json
import dicttoxml
from xml.dom import minidom


def json2xml():

    translatedjsonFile = jsontodictFile(readjson())
    translatedxmlFile = dicttoxmlFile(translatedjsonFile)
    print(translatedxmlFile)
    writexml(translatedxmlFile)
    parsexmlfile()
    
    # TargetFile = open('jsonfile.json','r')
    # readJsonTargetFile = json.load(TargetFile)
    # print(readJsonTargetFile)
    # transJson_to_xml = dicttoxml.dicttoxml(readJsonTargetFile)
    # print(transJson_to_xml)
    # TargetFile.close()
    # TransTargetFile = open('xmlfile.xml', 'r')
    # parsedTransTargetFile = minidom.parse(TransTargetFile)
    # TransTargetFile.write(parsedTransTargetFile)
    # TransTargetFile.close()
    
def readjson():
    TargetFile = open('jsonfile.json','r')
    return TargetFile

def writexml(writeFile):
    with open('xmlfile.xml', 'wb') as xmlFile:
        xmlFile.write(writeFile)

def parsexmlfile():
    # with open('xmlfile.xml', 'wb') as parsexmlFile:
    parsedTransTargetFile = minidom.parse('xmlfile.xml')
    with open('xmlfile.xml', 'wt') as xmlFile:
        xmlFile.write(parsedTransTargetFile.toxml())
    # writexml(parsedTransTargetFile.toxml())
    # writexml(parsedTransTargetFile)


def jsontodictFile(Targetfile):
    translateddictFile = json.load(Targetfile)
    return translateddictFile

def dicttoxmlFile(Targetfile):
    translatedxmlFile = dicttoxml.dicttoxml(Targetfile)
    return translatedxmlFile

if __name__=='__main__':
    json2xml()
