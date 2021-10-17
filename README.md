# NOBITA
NOBITA stands for Numericalization Of Brightness of Image for One Touch Assessment. You can upload an image taken with your phone and click on a desired location to display the brightness of there. This was created to support the analysis of RT_LAMP results, but can be used in the same way for other fluorescence images.
# DEMO
All you have to do is  just to upload the image and click on the location where you want to know the brightness.
For detailed instructions, see "tutorial_of_NOBITA.docx".

# Requirement
* Users of mac

    Just double-click on NOBITA/dist/nobita to use it.

* Non-mac users, or those who have had trouble with the above methods

    - Python3
    - Pillow

# Installation
* If you are a non-mac user, or if the above method did not work for you, please run the following to install the necessary libraries, etc.
    - Download and install Python3 from https://www.python.org.
    - Type the following command on the command line to install the image processing library Pillow.

    ```bash
    pip install Pillow
    ```

    - Run NOBITA/nobita.py. The first screen will be displayed.

 
# Usage
* Users of mac

    Double-click on NOBITA/dist/nobita to use it.
* If you are not a mac user, or if the above methods did not work for you


    Type the following command.
```bash
git clone https://github.com/igemsoftware2021/Kyoto_NOBITA.git
cd NOBITA
python3 nobita.py
```
 
# Note
 
Only RGB images can be used; 4-channel images such as RGBA and black and white images cannot be used.
 
# Author
 
* Producer : Kaho Tanaka
* Affiliation : Team:iGEM Kyoto 2021
* E-mail : igemkyoto2021@gmail.com
 
# License
NOBITA is OSS. Everyone can use this software without any permission.