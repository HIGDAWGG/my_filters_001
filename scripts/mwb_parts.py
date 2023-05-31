import os, sys, string

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("source",help="Where the MWB is")
parser.add_argument("outdir",help="Where to save to")
args = parser.parse_args()

mwb_parts = {

}

mwb_file = open(args.source,encoding="UTF-8")
mwb = mwb_file.read().split("\n")
mwb_file.close()

part_name = ""
titlearea = ""

print(os.getcwd())

include_list = None
def include_list(path,parentpath):
    reldir = os.path.split(parentpath)[0]
    includepath = os.path.join(reldir,path)
    try:
        includecontentfile = open(includepath,encoding="UTF-8")
        includefilecontent = includecontentfile.read()
        includefilecontentlines = includefilecontent.split("\n")
        includecontent = ""
        for l in includefilecontentlines:
            if l.startswith("!#include"):
                includecontent += include_list(l[10:],includepath)
            else:
                includecontent += l + "\n"
        includecontentfile.close()
        return includecontent + "\n"
    except Exception as err:
        print(err,includepath)
        return ""

for l in mwb:
    if l.startswith("! ---- "):
        part_name = l[6:-5]
        mwb_parts[part_name] = ""
    elif part_name == "":
        titlearea += l + "\n"
    elif l.startswith("!#include "):
        includepath = l[10:]
        mwb_parts[part_name] += include_list(includepath,args.source)
    else:
        mwb_parts[part_name] += l + "\n"

for part in mwb_parts:
    partfilename = os.path.join(args.outdir,part)
    partfile = open(partfilename,'w',encoding="UTF-8")
    partfile.write(titlearea)
    partfile.write(mwb_parts[part])
    partfile.close()
