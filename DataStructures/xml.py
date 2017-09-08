import xml.etree.ElementTree as etree
import sys


def xml_stats(xml_tree):
    root = xml_tree.getroot()
    print("Tag ", root.tag)
    print("Number of children: ", len(root))
    for child in root:
        print(child)
    print("Attributes:\n", root.attrib)

if __name__=='__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    xml_stats(tree)
