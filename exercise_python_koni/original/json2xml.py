import json
import xmltodict

def main():
    TargetFile = open('jsonfile.json','r')
    readJsonTargetFile = json.load(TargetFile)
    print(readJsonTargetFile)
    transJson_to_xml = xmltodict.unparse(readJsonTargetFile)
    # print(transJson_to_xml)
    TargetFile.close()
if __name__=='__main__':
    main()
