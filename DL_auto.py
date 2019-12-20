import os

ext = {
    "image": ['.jpg','.png','.jpeg','.tif','.gif'],
    "documents": ['.docx','.pdf','.doc'],
    "zips": ['.zip','.tar.gz','.tgz'],
    "python": ['.py','.ipynb','.pyc','.pyo'],
    "application": ['.exe']
}

dirs = {
    "image": "my_images",
    "documents": "my_documents",
    "zips": "zip_files",
    "python": "python_files",
    "application": "Applications"
}

src = os.path.expanduser(os.path.join('~',"Downloads"))

files = [x for x in os.listdir(src) if os.path.isfile(os.path.join(src, x))]
for f in files:
    filename, file_extension = os.path.splitext(f)
    for extension in ext.keys():
        if file_extension in ext[extension]:
            print("found it! {0} is of type {1}".format(f, extension))
            os.rename(os.path.join(src, f), os.path.join(src, dirs[extension], f)) 
            break

