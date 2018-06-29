import re
import os
import sys
from pprint import pprint

projectDir = "./proj1"


def getFilesUtils(dirs, files, filePath):
    if type(dirs) is tuple: 
        filePath = dirs[0]
        for dir_ in dirs:
            getFilesUtils(dir_, files, filePath)
            
    elif type(dirs) is list:
        for file in dirs:
            getFilesUtils(file, files, filePath+"/"+file)
        
    elif type(dirs) is str:
        if dirs.endswith(".html"):
            return files["htmlFiles"].update(dict({filePath:set()}))
            
        elif dirs.endswith(".css"):
            return files["cssFiles"].update(dict({filePath:set()}))
        elif dirs.endswith(".js"):
            return files["jsFiles"].update(dict({filePath:set()}))

        
def getFiles():       
    files = {
        "htmlFiles": dict(),
        "cssFiles": dict(),
        "jsFiles": dict(),
    }
    for dirs in os.walk(projectDir):
         getFilesUtils(dirs, files, "") 
    
    return files



def getHTMLClassesTagsIds(files):
    for htmlFile in files['htmlFiles']:
        with open(htmlFile) as f:
            matches= set()
            for line in f.readlines():
                #classes
                classes = [text_find.split() 
                               for text_find in re.findall(r'class[ ]{0,1}\=[ ]{0,1}[\'\"]{1}([ a-zA-Z0-9/_/-]+)[\'\"]{0,1}', line) 
                                   if len(text_find) > 0]
                
                classes = {clas for class_list in classes for clas in class_list}
                for cls in classes:
                    matches.add("." + cls)
                
                #ids
                ids = [text_find.split() 
                               for text_find in re.findall(r'id[ ]{0,1}\=[ ]{0,1}[\'\"]{1}([ a-zA-Z0-9/_/-]+)[\'\"]{0,1}', line) 
                                   if len(text_find) > 0]
                ids = {id_ for id_list in ids for id_ in id_list}
                for id_ in ids:
                    matches.add("#" + id_) 
                    
                #tags
                tags = [text_find.split() 
                               for text_find in re.findall(r'<[ ]*([a-zA-Z0-9]+)', line) 
                                   if len(text_find) > 0]
                tags = {tag for tag_list in tags for tag in tag_list}
                for tag in tags:
                    matches.add(tag)  
                    
            files['htmlFiles'][htmlFile] = matches
     
    
def getJSClassesTagsIds(files):
    for htmlFile in files['cssFiles']:
        with open(htmlFile) as f:
            matches= set()
            for line in f.readlines():
                #classes
                classes = [text_find.split() 
                               for text_find in re.findall(r'class[ ]{0,1}\=[ ]{0,1}[\'\"]{1}([ a-zA-Z0-9/_/-]+)[\'\"]{0,1}', line) 
                                   if len(text_find) > 0]
                
                classes = {clas for class_list in classes for clas in class_list}
                for cls in classes:
                    matches.add("." + cls)
            files['htmlFiles'][htmlFile] = matches


def getCSSClassesTagsIds(files):
    for cssFile in files['cssFiles']:
        with open(cssFile) as f:
            data=f.read().replace('\n', '')
            matches = [text_find.split() 
                               for text_find in re.findall(r'[\. \#]([ \=\"\'\[\]\(\)a-zA-Z0-9\-\:\>\,/_]+)[ \n]*\{', data) 
                                   if len(text_find) > 0]
            print(cssFile)
            print(matches, "\n\n\n\n\n\n")
            
            #\#\[\]\(\)
#             classes = {clas for class_list in classes for clas in class_list}
#             for cls in classes:
#                 matches.add("." + cls)
#             files['htmlFiles'][htmlFile] = matches
        
        
def main():
    files = getFiles()
    getHTMLClassesTagsIds(files)
    getCSSClassesTagsIds(files)
#     pprint(files)
    
    
if __name__ == "__main__":
    main()