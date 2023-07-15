import os
import shutil

absolutePath = '/home/stecher/Documents/pyfile'
imagesPath = '/home/stecher/Documents/pyfile/imgs'
foldersPath = '/home/stecher/Documents/pyfile/folders/'

images = os.listdir(imagesPath)
imgArr = []
folderI = 0

# Folder Creation
# for f in range(1, 99):
#     os.makedirs(foldersPath + str(f))

for i, name in enumerate(images):
    imgArr.append(name)
    if len(imgArr) == 62:
        for j, imarrName in enumerate(imgArr):
            shutil.move(imagesPath + "/" + imarrName, foldersPath + str(26 + folderI) + "/" + imarrName)
            print("Moved", imarrName, "to", str(26 + folderI))
        folderI += 1
        imgArr.clear()
