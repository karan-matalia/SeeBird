# SeeBird

## Installation Guidelines

### Pre-requisites

1. Download and install Python from the following url: https://www.python.org/downloads/
2. Download and install Anaconda from the url: https://www.anaconda.com/products/individual.
3. Download and install Google Chrome. If you already have it update it to the latest version. To update your Google Chrome open Chrome and type `chrome://settings/help` in your address bar. You can upadte your Chrome from here. Once that is done note down the Chrome version. It would be something like: `Version 84.0.4147.89 (Official Build) (64-bit)`.
4. Download and install Chromedriver from the url: https://chromedriver.chromium.org/downloads. Download the version that corresponds to the Google Chrome version that you found in step 3.
5. Download and install Pycharm Community Edition from the url: https://www.jetbrains.com/pycharm/download/

## How to download and setup the software

**Step 1.** Download a zip file for the code from this url: `https://github.com/karan-matalia/SeeBird/archive/master.zip`. Once downloaded extract it to a folder of your choice.
** Step 2.** Open Pycharm and then click on the Open button on the right hand side.<br>

  ![Step 2](https://github.com/karan-matalia/SeeBird/blob/master/res/Annotation%202020-07-18%20142301.png)
  
**Step 3.** Then you have to select the folder that you had just extracted and click on Ok button.<br>
  ![Step 3](https://github.com/karan-matalia/SeeBird/blob/master/res/Annotation%202020-07-18%20142610.png)
  
**Step 4.** Then pycharm will show a message on the right hand side to configure a Python interpretor. Click on the blue text. If you are able to click on it you can skip step 5.
  ![Step 4](https://github.com/karan-matalia/SeeBird/blob/master/res/Annotation%202020-07-18%20142654_LI.jpg)
  
**Step 5.** If you do not get the message then on the top bar click on `File` and then click on `Settings`. Inside the settings menu, at the top there will be a search bar. In the search bar type `Python Interpretor`. Click on `Python Interpretor` from the options. You will get a page like this but empty. At the top section of of the page There will be a project interpretor dropdown. Click on that dropdown.<br>
  ![Step 5.1](https://github.com/karan-matalia/SeeBird/blob/master/res/Annotation%202020-07-18%20145557.png) <br>
  You will get another menu. On the right hand side of that menu you will see a `+` sign, click on that.<br>
  ![Step 5.2](https://github.com/karan-matalia/SeeBird/blob/master/res/Annotation%202020-07-18%20145637.png)
  
**Step 6.** You will get a page to configure your python interpretor. On the list on the left hand side. Select `Conda Environment`. Then make sure that at the top `new environment` button is selected. Also make sure that pyhton version is what you have downloaded. Then click on OK button. <br>
![Step 6](https://github.com/karan-matalia/SeeBird/blob/master/res/Annotation%202020-07-18%20142805_LI.jpg)

**Step 7.** Come back to the home page. At the bottom bar you will see a button for `Terminal` click on that. Then when it's open type this command `pip install -r requirements.txt` and then press enter key. Wait for all installations to complete. <br>
  ![Step 7](https://github.com/karan-matalia/SeeBird/blob/master/res/Annotation%202020-07-18%20145310_LI.jpg)
  
**Step 8.** On the left hand side in the `Project Structure` section click on the `SeeBird` dropdown. Then click on `src` and then open the file `utils.py`. Then press `Ctrl F` or `Cmd F` and type in `C:\Users\admin\Downloads\chromedriver.exe`. It will highlight the txt for you. Then go to the highlighted text and remove the text `C:\Users\admin\Downloads\chromedriver.exe`. But do not remove the `"` symbols on each side. Then open the folder where you have downloaded Chromedriver. Select the path of the folder and copy it in between the two `""` symbols. Also add the text `chromedriver.exe` at the end before the last `"` sign. Once that is done a couple of lines below you will see the text `your-username` and `your-password`. Replace it with your ebird username and password. Do not remove the `"` symbol again. Do not worry your details will be safely present on your machine only. <br>
  ![Step 7](https://github.com/karan-matalia/SeeBird/blob/master/res/Annotation%202020-07-18%20154241.png)
  
**Step 9.** Whew that were a lot of steps! This is one final step to start the program. On the left hand side in the `Project Structure` section open the file `driver.py`. Beside the text `if __name__ == '__main__':` there will be a green play button click on that. Then at the bottom a Run section will open where you first click inside it and then start using the program. <br>
  ![Step 7](https://github.com/karan-matalia/SeeBird/blob/master/res/Annotation%202020-07-18%20145350.png)


## How to use the software after running it

When you press the green play button you will see a new window in your screen with a menu that shows 9 options. Click on that window and type in the number for the data that you want to see. Once you press the number and click enter a new Chrome windows will open if you have done the setup correctly or else you will see some error message in red coloured text.If the Chrome window opens you can wait for a few seconds and your data will be displayed.
