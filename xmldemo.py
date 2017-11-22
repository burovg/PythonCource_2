from xml.dom import minidom

doc = minidom.parse("c:\\temp\\test.xml")
arr = doc.getElementsByTagName("book")
for book in arr:
    company = book.getElementsByTagName("Company")
    if len(company) > 0:
        address = company[0].getElementsByTagName("Address")
        if len(address) > 0:
            print address[0].firstChild.data


address = doc.getElementsByTagName("Address")
for a in address:
   print a.firstChild.data




