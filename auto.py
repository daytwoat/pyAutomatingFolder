from distutils import filelist
import os
import collections
#####################
# extation
holak = {
"Compressed" :['iso','zip', 'tar', 'torrent', 'rar', '7z'],
"Documents" : ['txt', 'pdf', 'csv', 'xls', 'doc', 'docx', 'html','ppt', 'pptx'],
"Music" : ['mp3','wav'],
"Programs" :['exe','msi','apk'],
"Videos" :['mp4','avi','mkv','mov','mpg','h264'],
"Images" : ['png','jpg','jpeg','gif','ico','bmp','webp','PNG']
}

#main path
base_path = os.path.expanduser('~')
downloads_path = os.path.join(base_path, 'Downloads')
dest_dirs = [ 'Programs','Documents','Music','Videos','Images','Compressed','Others']

for d in dest_dirs:
    dir_path = os.path.join(downloads_path, d)
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)
        
# mapping files
files_mapping = collections.defaultdict(list)
files_list = os.listdir(downloads_path)

extn = holak.values()
for f in files_list:
    for x in list(holak.values()):
            for xx in x:
                if( xx== f.split('.')[-1]):
                    foldername = [k for k, v in list(holak.items()) if xx in v]
                    os.rename(os.path.join(downloads_path, f), os.path.join(downloads_path, foldername[0] ,f))
