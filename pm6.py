#!/usr/bin/python

import urllib2
import re
import json
#content_stream = urllib2.urlopen('http://www.6pm.com/grazie-flossie-red')
#content = content_stream.read()
with open(r'red.txt') as somefile:
        content =  somefile.read()
            # ...more code
#print content
#var dimensions = ["d3","d4"];


# getproductId
def reslove(url):


    content_stream = urllib2.urlopen(url)
    content = content_stream.read()

    print '''<hr>'''
    print '''<table>
          <tr>

    '''

    productId =  re.search(r'(var[\s]productId[\s]*\=)([^;]+)',content).group(2)
    print "<th> ", productId, "</th>"

    productName =  re.search(r'(var[\s]productName[\s]*\=)([^;]+)',content).group(2)
    print "<th> ",productName, "</th>"

    brandName  =  re.search(r'(var[\s]brandName [\s]*\=)([^;]+)',content).group(2)
    print "<th> ",brandName, "</th>"
    print "</tr>"


    colorNames  =  re.search(r'(var[\s]colorNames [\s]*\=)([^;]+)',content).group(2)
    colorNames =  colorNames.replace("\n", "").strip().replace("\'","\"")
    #print colorNames
    colorNames = json.loads(colorNames)
    #print  colorNames.replace("\n", "");
    #print "colorNames  is ", colorNames 


    dimensions = re.search(r'(dimensions[\s]*\=)([^;]+)',content).group(2)
    dimensions = json.loads(dimensions)
    for dimen in dimensions:
        print dimen
        

    valueIdToName = re.search(r'(valueIdToNameJSON[\s]*\=)([^;]+)',content).group(2)
    valueIdtoNameJson = json.loads(valueIdToName)
    #print valueIdtoNameJson

    stock =  re.search(r'(stockJSON[^;]+)',content).group().split("=")
    test = json.loads(stock[1])

    imgs = re.search(r'(http://[^\s]*MULTIVIEW.jpg)',content).group()
    print "<tr><td cols=3><img src='",imgs,"' /></td></tr>"
    #print test
    for item in test:
        for dimen in dimensions:
           #print "color:", colorNames[item["color"].encode('utf-8')], "size" ,valueIdtoNameJson[item[dimen]]["value"]," stock ",item["onHand"]
           print '''
              <tr>
                <td>''',colorNames[item["color"].encode('utf-8')],'''</td>
                <td>''',valueIdtoNameJson[item[dimen]]["value"],'''</td>
                <td>''',item["onHand"],'''</td>
              </tr>
           '''
    print "</table>"
        


if __name__=="__main__":
    with open(r'urls.txt') as somefile:
    	for line in somefile:
    		reslove(line)
    		

#var colorNames = {
#'3':"Black",
#'158':"Blue",
#'401':"Grey",
#'574':"Purple",
#'585':"Red"
#}
#;



