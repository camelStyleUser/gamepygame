import os,random
from zipfile import ZipFile
id=random.randint(1,1858747828)
id=str(id)
zipcont="""
"""
fd=open("tmp"+id+.zip","w")
fd.write(zipcont)
fd.close()
zObj=ZipFile(os.getcwd()+os.sep+"tmp"+id+".zip")
zObj.extractall(os.getcwd()+os.sep+"tmp"+id)
zObj.close()
os.chdir((os.getcwd()+os.sep+"tmp"+id)
os.system("main.exe")
