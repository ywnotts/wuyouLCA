#!/usr/bin/env python
# -*- coding: utf-8 -*-
# WRITE all values & modification following QI
# coding = gbk
# produce data without names

import os
import xml.etree.cElementTree as ET

def xml_open(path):
    items = os.listdir(path)
    new_items = []
    for f in items:
        f_name, f_suffix = os.path.splitext(f)
        if f_suffix == ".XML":
           new_items.append(f_name+f_suffix)
    return new_items

def xml_data_capture(path):
    xml_results = []
    for i in xml_open(path):
        tree = ET.ElementTree(file=i)
        root = tree.getroot()
        dataset = (root[0].attrib)
        key_dataset = {'number'}
        number = str(dataset.get('number'))
        referenceFunction = (root[0][0][0][0].attrib)
        category = str(referenceFunction.get('category'))
        subCategory = str(referenceFunction.get('subCategory'))
        name = referenceFunction.get('name').encode("utf-8")
        CASNumber = str(referenceFunction.get('CASNumber'))
        unit = str(referenceFunction.get('unit'))
        amount = str(referenceFunction.get('amount')) 
        geography = (root[0][0][0][1].attrib)
        location = str(geography.get('location'))
        #content = number + "^" + category + "^" + subCategory + "^" + name + "^" + CASNumber + "^" + unit + "^" + amount + "^" + location
        #改成元组
        content =( number , category , subCategory , name , CASNumber , unit , amount , location)
        xml_results.append(content)
    return xml_results
        
            
        
if __name__ == "__main__":
    file_path = r"C:\Users\dsg3wuy\Desktop\test"
    xml_results_list = xml_data_capture(file_path)

import csv
with open("test2.csv","ab") as w:
    writer = csv.writer(w,dialect="excel")
    for r in xml_results_list:
        writer.writerow(r)
            
    print "ok, DONE."
