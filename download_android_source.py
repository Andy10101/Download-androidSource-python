# -*- coding: utf-8 -*-
import json
import os
import commands
class JSONParse ():
        
    def __init__(self, file_name):
        self.json = None;
        try:
            fp = open(file_name)
            # print fp.read();
            self.json = json.loads(fp.read(), encoding="utf-8");
        except StandardError:
            print "Error json";
        

        pass   
    def command(self, cmd):
        
        status, output = commands.getstatusoutput(cmd)
        # print status
        print output
        
        pass
    

if __name__ == '__main__':
        dirName = "/Users/haizhu/Documents/Android/SDK/source_code";
        tag_name = " android-l-preview_r2"
        jsonParse = JSONParse("googlesource.json")
        count = 0;
        for line in  jsonParse.json:
             name = jsonParse.json.get(line).get("name");
             url = jsonParse.json.get(line).get("clone_url");
             count += 1;
             savePath = dirName + "/" + name;
             print "\n\n\n"
             print count
             if os.path.exists(savePath):
                 cmd = "cd " + savePath + "\n";
                 cmd += "git pull \n"
             else :
                 cmd = "cd " + dirName + "\n";
                 cmd = "git clone " + url + "  " + savePath + " \n";                          
             cmd += "git checkout  " + tag_name;
            
             print cmd
             
             jsonParse.command(cmd);
             
                         
        print count;  
        pass
        
        
        
