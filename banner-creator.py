import pyfiglet
from PIL import Image
import shutil
import numpy as np
import argparse
import platform
import os

parser = argparse.ArgumentParser(description = "Banner Creator, a python CLI tools that help you to create banners")

parser.add_argument("-t", "--title", type = str, metavar = "<text>", help = "The text string you want to use as a banner")

parser.add_argument("-i", "--image", type = str, metavar = "<file_path>", help = "File path to the image you want to use as a banner")

parser.add_argument("-g", "--gamma", type = float, metavar = "<float>", help = "Manually set the gamma value to adjust brightness. Use > 1.0 to darken (increase contrast) or < 1.0 to brighten. This overrides the auto-detection.")

parser.add_argument("-p", "--plain-text", type = str, metavar = "<file_path>", help = "File path to a plain_text text file used as a startup message for new terminal sessions")

parser.add_argument("-s", "--set-banner", action = "store_true", help = "Set the generated outputs as terminal banner")

parser.add_argument("-r", "--remove-banner", action = "store_true", help = "Remove the banner from terminal")

args = parser.parse_args()

outputs = []

if args.title:

    print()
    banner = pyfiglet.figlet_format(args.title)
    print(banner) # banner includes a line break at the end

    if args.set_banner:
        outputs.append("\n" + banner + "\n")

if args.image:

    img = Image.open(args.image)

    colums = shutil.get_terminal_size()[0] * 0.8
    rows = shutil.get_terminal_size()[1] * 0.8

    # print("Colums", colums)
    # print("Rows", rows)

    width, height = img.size
    width  = width * 2

    # print("Width : ", width)
    # print("Height : ", height)

    cut1 = colums / width
    cut2 = rows / height 

    if cut1 <= cut2 and cut1 < 1:
        width = colums 
        height *= cut1

    if cut2 < cut1 and cut2 < 1:
        height = rows 
        width *= cut2

    # print("Resized Width : ", width)
    # print("Resized Height : ", height)

    width = round(width)
    height = round(height)

    img = img.resize((width, height), resample = Image.LANCZOS)
    img = img.convert("L")
    # img.show()

    pixels = list(img.get_flattened_data())
    # print(pixels)

    s = ".:-=+*#%@"

    minn = min(pixels)
    maxn = max(pixels)

    def minmax(x):
        if maxn == minn: return x / 255
        return (x - minn) / (maxn - minn) 

    asciis = []
    median = np.median(pixels)

    if args.gamma:
        gamma = args.gamma

    else:
        gamma = 1
        if median > 150:
            gamma = 2
        elif median < 80:
            gamma = 0.5

    for i in pixels:
        asciis.append(s[round((minmax(i) ** gamma) * (len(s) - 1))])


    # print(len(pixels))
    # print(width * height)

    temp = ""

    if args.title == None: 
        print()
        outputs.append("\n\n")

    for i in range(len(pixels)):
        print(asciis[i], end = "")
        temp += asciis[i]
        if (i + 1) % width == 0:
            print()
            if args.set_banner:
                outputs.append(temp)
                outputs.append("\n")
            temp = ""
    print()
    if args.set_banner:
        outputs.append("\n")
    

if args.plain_text:
    
    if args.title == None and args.image == None: 
        print()
        outputs.append("\n")

    with open(args.plain_text, "r") as f:
        plain_lines = f.readlines()

    for i in plain_lines:
        print(i, end = "")
        if args.set_banner:
            outputs.append(i)

    print("\n")
    if args.set_banner: outputs.append("\n")

if args.title == None and args.image == None and args.plain_text == None:
    print()

if args.title == None and args.image == None and args.plain_text == None and args.remove_banner == False:
    print("Reminder : You have to enter the parameters\n")
elif args.title == None and args.image == None and args.plain_text == None and args.set_banner == True:
    print("Reminder : You have to enter the parameters\n")
else:
    bashrc_path = os.path.expanduser("~/.bashrc")
    banner_path = os.path.expanduser("~/.banner_save.txt")
    current_os = platform.system()

    if args.remove_banner:
        if current_os == "Linux":

            with open(bashrc_path, "r") as f:
                bashrc_content = f.readlines()

            deletes = ["# --- BANNER CREATOR START ---", f"cat {banner_path}", "# --- BANNER CREATOR END ---"]
            new_bashrc_content = []

            for i in bashrc_content:
                if deletes[0] in i: continue 
                if deletes[1] in i: continue
                if deletes[2] in i: continue 
                new_bashrc_content.append(i)

            with open(bashrc_path, "w") as f:
                for i in new_bashrc_content:
                    f.write(i)
            print("Banner successfully removed!\n")
        else:
            print("Error: The --remove-banner feature is currently only supported on Linux\n")

    if args.set_banner:
        if current_os == "Linux":  
            
            with open(bashrc_path, "r") as f:
                bashrc_content = f.readlines()

            is_set = False

            for i in bashrc_content:
                if "# --- BANNER CREATOR START ---" in i:
                    print("Banner is already set in ~/.bashrc. (Use -r to clear it first)")
                    is_set = True
                    break

            if not is_set:
                with open(banner_path, "w") as f:
                    for i in outputs:
                        f.write(i)

                needs_newline = False
                if len(bashrc_content) > 0 and not bashrc_content[-1].endswith("\n"):
                    needs_newline = True
                    
                with open(bashrc_path, "a") as f:
                    if needs_newline:
                        f.write("\n")
                    f.write("# --- BANNER CREATOR START ---\n")
                    f.write(f"cat {banner_path}\n")
                    f.write("# --- BANNER CREATOR END ---\n")
                print("Banner successfully set!\n")

        else:
            print("Error: The --set-banner feature is currently only supported on Linux\n")
    