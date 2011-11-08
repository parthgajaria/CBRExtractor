import UnRAR2
import os
import sys

rootdir = sys.argv[1]
for root, subFolders, files in os.walk(rootdir):
	for file in files:
		if(file[-4:] == ".cbr"):
			truecount = 0
			# Populates the list with all the file names in a given directory structure
			for fileInArchive in UnRAR2.RarFile(os.path.join(root,file)).infoiter():
				if (fileInArchive.isdir):
					truecount = truecount + 1
			if (truecount == 0):
				#Make a directory
				os.mkdir(os.path.join(os.path.abspath(rootdir), file[:-4]))
				#extract all the files in CBR
				UnRAR2.RarFile(os.path.join(root,file)).extract(path = os.path.join(os.path.abspath(rootdir), file[:-4]))
			else:
				#extract all the files in CBR
				UnRAR2.RarFile(os.path.join(root,file)).extract(path = os.path.abspath(rootdir))