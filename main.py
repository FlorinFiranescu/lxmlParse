from lxml import etree, objectify

def parseXML(xmlFile, xmlFileNew):
    #parse the xml from the inputed xmlFile
    with open(xmlFile) as f:
        xml = f.read()
    root = objectify.fromstring(xml)

    #add some custom attributes & tags to the xml
    id = 0
    for book in root.getchildren():
        book.bookNumber = "Book number " + str(id+1)
        book.set("idNumber", str(id))
        id = id + 1
        print("Attributes : " + str(book.attrib))
        for item in book.getchildren():
            print(f"{item.tag} <=> {item.text}")

    # remove the py:pytype & xmlns:py additional content
    objectify.deannotate(root)
    etree.cleanup_namespaces(root)
    obj_xml = etree.tostring(root, pretty_print=True, encoding="unicode")
    print(obj_xml)

    # save the xml to xmlFileNew
    with open(xmlFileNew, "w") as f:
        f.write(obj_xml)


if __name__ == "__main__":
    parseXML("books.xml", "booksNew.xml")