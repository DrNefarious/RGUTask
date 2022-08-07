import os # For general commands
import xml.etree.ElementTree as ET # To parse the xml file
from flask import Flask, jsonify # To create web server API and to create json response


# The following two classes are used to parse the xml file into a Python dictionary structure
# Python dictionaries require uniqueness so sometimes a list is required
# The classes are called recursively until the bottom of the xml tree is reached
# The code is loosely based on code found at https://code.activestate.com/recipes/410469-xml-as-dictionary/, although that code was broken so I had to fix it
# There are absolutely simpler ways of doing it, but I wanted to use ElementTree, and became determined to make it work :)

# If the element has non-unique children
class XmlListParse(list):
    def __init__(self, element):
        # Iterate though the children of the provided element
        for child in element:
            if len(child):
                # If children are unique use a dictionary structure
                if len(child) == 1 or child[0].tag != child[1].tag:
                    self.append(XmlDictParse(child))
                # If children are not unique use a list structure
                elif child[0].tag == child[1].tag:
                    self.append(XmlListParse(child))
            # Add any attributes the child element has
            elif child.items():
                self.append(dict(child.items()))
            # Add any text the child element contains (not needed in this assignment)
            elif child.text:
                text = child.text.strip()
                if text:
                    self.append(text)

# If the element has unique children
class XmlDictParse(dict):
    def __init__(self, element):
        childrenNames = []

        for child in element.getchildren():
            childrenNames.append(child.tag)
        if element.items():
            self.update(dict(element.items()))

        # Iterate though the children of the provided element
        for child in element:
            if len(child):
                # If children are unique use a dictionary structure
                if len(child) == 1 or child[0].tag != child[1].tag:
                    tempDict = XmlDictParse(child)
                # If children are not unique use a list structure
                else:
                    tempDict = {child[0].tag: XmlListParse(child)}
                # Add any attributes the element has
                if child.items():
                    tempDict.update(dict(child.items()))
                # This is required to ensure that the dictionary structure properly appends new info instead of replacing old info
                if childrenNames.count(child.tag) > 1:
                    try:
                        currentValue = self[child.tag]
                        currentValue.append(tempDict)
                        self.update({child.tag: currentValue})
                    except: 
                        self.update({child.tag: [tempDict]})
                else:
                    self.update({child.tag: tempDict})
            elif child.items():
                self.update({child.tag: dict(child.items())}) # Append child attributes
            else:
                self.update({child.tag: child.text}) # Append child text

# Main
tree = ET.parse('cases.xml') # Parse xml file using ElementTree
root = tree.getroot() # Acquire root element
xmlData = XmlDictParse(root) # Create Python dictionary data structure containing the xml data from the ElementTree object

# Create and configure the flask app
app = Flask(__name__)

# Create API endpoint /scores, and return Python dictionary containing XML data
@app.route('/scores', methods=['GET'])
def scores():
    response = jsonify(xmlData) # Format data structure as JSON
    response.headers.add('Access-Control-Allow-Origin', '*') # To allow requests from same location
    return response