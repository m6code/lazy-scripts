# batch_add_file_extension.py
import os
import shutil
from PIL import Image

def main():
    copy_spotlight_files()
    add_img_ext()
    sort_images()


def add_img_ext():
    root = os.getcwd()
    for file in os.listdir('.'):
        if not os.path.isfile(file):
            continue
        # get the file name and extenstion
        name, ext = os.path.splitext(file)
        # print(name, ext)
        if not ext:
            src = os.path.join(root, file)
            dst = os.path.join(root, file + '.jpg')

            if not os.path.exists(dst):
                os.rename(src, dst)
            else:
                os.remove(src)

# ADD The Ability to Move portrait images to the portraits folder
def sort_images():
    root = os.getcwd()
    if root[-1] != '/':
        root = root + '/'
    # Create the portrait directory
    portrait_dir = root + "/portrait"
    landscape_dir = root + "/landscape"
    if not os.path.exists(portrait_dir):
        os.makedirs(portrait_dir)
    if not os.path.exists(landscape_dir):
        os.makedirs(landscape_dir)

    for file in os.listdir("."):
        if not os.path.isfile(file):
            continue
        image_path = root + file
        name, ext = os.path.splitext(file)
        if ext in [".jpg", "jpeg", "png"]:
            with Image.open(image_path) as image:
                width, height = image.size
            # print(width, height)
            if width < height:
                # move portrait image to portrait folder
                try: 
                    shutil.move(image_path, portrait_dir)
                    print(f"Moved {image_path} --> {portrait_dir}")
                except:
                    print(f"Error moving {image_path}")
                    os.remove(image_path)
                    pass
            else:
                # landscape: move to landscape folder
                try: 
                    shutil.move(image_path, landscape_dir)
                    print(f"Moved {image_path} --> {landscape_dir}")
                except:
                    print(f"Error moving {image_path}")
                    os.remove(image_path)
                    pass
           

# Copies microsoft spolight images
def copy_spotlight_files():
    # shutil.copytree("C:\\Users\\Benfr\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets", os.getcwd())
    # src = "C:\\Users\\Benfr\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets"
    src = f"{os.environ['USERPROFILE']}\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets"
    trg = os.getcwd()

    files = os.listdir(src)

    for file in files:
        shutil.copy2(os.path.join(src,file), trg)

if __name__ == "__main__":
    main()
