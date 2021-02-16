import json
import dicttoxml

def main():
    TargetFile = open('jsonfile.json','r')
    readJsonTargetFile = json.load(TargetFile)
    # print(readJsonTargetFile)
    transJson_to_xml = dicttoxml.dicttoxml(readJsonTargetFile)
    # print(transJson_to_xml)
    TargetFile.close()
    TransTargetFile = open('xmlfile.xml', 'wt')
    print(transJson_to_xml, file=TransTargetFile)
    TransTargetFile.close()

if __name__=='__main__':
    main()
