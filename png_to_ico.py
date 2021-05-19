import os
import shutil

yon=input('Do you want the PNG files to be deleted after conversion? (enter)')

def ico_convert(filename):
    from PIL import Image
    img=Image.open(png_path+filename)
    filename=filename.replace(filename[len(filename)-4:],'.ico')
    img.save(ico_path+filename, format='ico')

png_list=[]
ico_list=[]
ico='.ico'
this_file='png to ico.py'
dir_path = os.path.dirname(os.path.realpath(__file__))
png_path = dir_path+'\PNG/'
ico_path=dir_path+"\ICO/"

for entry in os.listdir(png_path):
    if os.path.isfile(os.path.join(png_path, entry)):
        entry=entry[:len(entry)-4]
        png_list.append(entry)

for entry in os.listdir(ico_path):
    if os.path.isfile(os.path.join(ico_path, entry)):
        entry=entry[:len(entry)-4]
        ico_list.append(entry)

br=0
convert=[]

for file in png_list:
    if file in ico_list:
        png_list.remove(file)
   
for file in png_list:
    if file not in ico_list:
        ico_convert(file+'.png')
        br+=1
        convert.append(file)

if br==0:
    print('No files have been converted!')

else:
    print('The following files have been converted:')
    for i in range (len(convert)):
        print(convert[i]+'.png')

if yon=='':
    shutil.rmtree(png_path)
    directory='PNG'
    dirName=dir_path
    path = os.path.join(dirName, directory)
    os.mkdir(path)
else:
    print ('Your files will not be deleted!')
    



    
