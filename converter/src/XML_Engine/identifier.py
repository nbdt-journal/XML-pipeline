from article_graph import article_node
import xml.etree.ElementTree as ET

if __name__ == '__main__':
    tree = ET.parse('sample.xml')
    root = tree.getroot()
    print(article_node.check(root))