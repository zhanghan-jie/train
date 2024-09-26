import os
import xml.etree.ElementTree as ET

xml="xml"
labels="labels"
class_id=["hat","head"]

def xml2txt():
    for i in os.listdir(xml):
        tree=ET.parse(os.path.join(xml+"/"+i))
        W=tree.find("size").find("width").text
        H=tree.find("size").find("height").text
        N=tree.find("filename").text[:-4]

        p=open(labels+"/"+N+".txt","w+")
        for obj in tree.iter("object"):
            xmin=obj.find("bndbox").find("xmin").text
            ymin=obj.find("bndbox").find("ymin").text
            xmax=obj.find("bndbox").find("xmax").text
            ymax=obj.find("bndbox").find("ymax").text

            classid=obj.find("name").text

            x=int(xmax)-int(xmin)
            y=int(ymax)-int(ymin)

            x_center=(int(xmax)+int(xmin))/2
            y_center=(int(ymax)+int(ymin))/2

            x=round(x/int(W),6)
            y=round(y/int(H),6)

            x_center=round(x_center/int(W),6)
            y_center=round(y_center/int(H),6)

            if classid=="hat":
                p.write("0"+" "+str(x_center)+" "+str(y_center)+" "+str(x)+" "+str(y)+" "+"\n")

            else:
                p.write("1" + " " + str(x_center) + " " + str(y_center) + " " + str(x) + " " + str(y) + " " + "\n")

xml2txt()
