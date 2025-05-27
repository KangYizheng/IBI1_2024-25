from xml.dom.minidom import parse
import xml.dom.minidom
import time
#DOM
#record time    
start_time = time.time()
DOMTree = xml.dom.minidom.parse(r"C:\Users\ASUS\Desktop\大一下学期\IBI1_2024-25\Practical14\go_obo.xml") # prase file
collection = DOMTree.documentElement # collect the document element
terms = collection.getElementsByTagName("term") # get the tag is term
# set the max dictionary
ontology_max1 = {
    "molecular_function": [],
    "biological_process": [],
    "cellular_component": []
}
max_count1 = {
    "molecular_function": 0,
    "biological_process": 0,
    "cellular_component": 0
}
for term in terms:
    namespace = term.getElementsByTagName("namespace")[0].firstChild.nodeValue #get the namespace
    go_id = term.getElementsByTagName("id")[0].firstChild.nodeValue # get the id
    name = term.getElementsByTagName("name")[0].firstChild.nodeValue# get the name
    is_a_list = term.getElementsByTagName("is_a") # get the all is_a
    count=len(is_a_list) # count the amount of is_a
    # update the dictionary
    if namespace in ontology_max1: 
        if count > max_count1[namespace]: # check if the count is greater than the max_count
            ontology_max1[namespace] = [(go_id, name, count)]
            max_count1[namespace] = count # update the max_count1 dictionary
        elif count == max_count1[namespace]: # store the same count
            ontology_max1[namespace].append((go_id, name, count))
print("Results from DOM parser:")
for ns, terms in ontology_max1.items():
    print(f"Ontology: {ns}")
    for go_id, name, count in terms:
        if count == max_count1[ns]:# check if the count is equal to the max_count
            # print the results
            print(f"  GO ID: {go_id}")
            print(f"  Name: {name}")
            print(f"  Number of <is_a>: {count}")
            print()


end_time = time.time()
dom_time = end_time - start_time # calculate the time taken
print(f"Time taken to parse XML using DOM: {dom_time:.2f} seconds")

#SAX
import xml.sax 
class GOHandler(xml.sax.ContentHandler): # create a class to handle the SAX parsing
    def __init__(self): # initialize the class
        self.current_element = "" # set the current element to empty
        self.go_id = "" # set the go_id to empty
        self.name = "" # set the name to empty
        self.namespace = "" # set the namespace to empty
        self.is_a_count = 0 # set the is_a_count to 0
        # set the max_counts dictionary to store the results for each namespace
        self.max_counts = {
        "molecular_function": [],
        "biological_process": [],
        "cellular_component": []
        }
        # set the max_values dictionary to store the maximum values for each namespace
        self.max_values = {
        "molecular_function": 0,
        "biological_process": 0,
        "cellular_component": 0
        }

        # set the temp variables to empty
        self.temp_name = ""
        self.temp_namespace = ""
        self.temp_id = ""
        # set the in_term and in_name to False
        self.in_term = False
        self.in_name = False

    def startElement(self, tag, attribute):# set the start element
        self.current_element = tag# set the current element to the tag
        if tag == "term":
            self.in_term = True # let the parser know we are in a term element
            self.go_id = "" # set the go_id to empty
            self.name = "" # set the name to empty
            self.namespace = "" # set the namespace to empty
            self.is_a_count = 0 # set the is_a_count to 0
            self.temp_namespace = ""# set the temp_namespace to empty
            self.temp_name = "" # set the temp_name to empty
            self.temp_id = "" # set the temp_id to empty
        if tag == "name":
            self.in_name = True # let the parser know we are in a name element
        elif self.current_element == "is_a": # check the if the current element is is_a
            self.is_a_count += 1
    def characters(self, content):
        if not self.in_term: 
            return
        if self.current_element == "id":# check the if the current element is id
            self.temp_id+= content
        elif self.current_element == "namespace": # check the if the current element is namespace
            self.temp_namespace += content
        elif self.in_name: # check the if the in_name is True
            self.temp_name += content

    def endElement(self, tag):
        if tag == "namespace":
            self.namespace = self.temp_namespace.strip() # set the namespace to temp_namespace
        
        elif tag == "id":
            self.go_id = self.temp_id.strip() # set the go_id to temp_id
        elif tag == "name":
            self.name = self.temp_name.strip() # set the name to temp_name
            self.in_name = False # let the parser know we are not in a name element anymore
        elif tag == "term": # update the max_counts dictionary
            if self.namespace in self.max_counts:
                if self.is_a_count > self.max_values[self.namespace]: # check if the is_a_count is greater than the max_values
                    self.max_counts[self.namespace] = [(self.go_id, self.name, self.is_a_count)]
                    self.max_values[self.namespace] = self.is_a_count
                elif self.is_a_count == self.max_values[self.namespace]: # check if the is_a_count is equal to the max_values
                    self.max_counts[self.namespace].append((self.go_id, self.name, self.is_a_count))
            self.in_term = False # let the parser know we are not in a term element anymore


# record start time
start_time = time.time()

# set up SAX parser
parser = xml.sax.make_parser()  # create an XMLReader
parser.setFeature(xml.sax.handler.feature_namespaces, False) # disable namespace handling
# set content handler
handler = GOHandler()# create an instance of the handler
parser.setContentHandler(handler)
# parse the XML file
parser.parse(r"C:\Users\ASUS\Desktop\大一下学期\IBI1_2024-25\Practical14\go_obo.xml")
# print results
print("Results from SAX parser:")
for ns, terms in handler.max_counts.items():
    print(f"Ontology: {ns}")
    for go_id, name, count in terms:
        if count == handler.max_values[ns]:# check if the count is equal to the max_values
            print(f"  GO ID: {go_id}")
            print(f"  Name: {name}")
            print(f"  Number of <is_a>: {count}")
            print()
# record end time
end_time = time.time()
sax_time = end_time - start_time
print(f"SAX parser took {sax_time:.4f} seconds.\n")
# print the time taken for SAX parser
# Comment recommendation:
# If you find one method faster:
if sax_time < dom_time:
    print("# SAX was faster.")
else:
    print("# DOM was faster.")