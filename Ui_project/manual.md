# Applications of ML in Mechatronics Tools GUI Technical Manual

This guide is prepared as a reference for you to know the necessary setup needed to operate the GUI. Additionally, it is meant to serve as a brief tutorial to help you understand some of the basics of the Raspberry Pi, esepecially if you are using it for a project.

# 1. Setup the Raspberry Pi

## 1.1. Prepare the Raspberry Pi (RPi) SD Card

The Raspberry Pi used in this course is a Raspberry Pi Zero W, where W stands for Wireless, which is the new version that has built-in WiFi and Bluetooth. Although WiFi is not strictly needed for the purpose of this application, it is used in this manual to make the setup easier and improve the overall useability.

### 1.1.1. Write the image to the SD Card

To run an operating system (OS) on the raspberry pi, you will need to burn it onto the SD card. Follow the following steps to burn the OS image:

1. Download and install the **Raspberry Pi Imager** from [here](https://www.raspberrypi.org/software/)
2. Run the imager
3. For the operating system, choose **Raspberry PI OS (Other)** and then **Raspberry Pi OS Lite**
4. For the SD Card, insert the micro-SD card into your computer and select it
5. Click **Write**

### 1.1.2. Enable Wireless Networking

To enable wireless networking, you will need the RPi to connect to your local wireless network. This will allow you to access the RPi from your computer through SSH.

You will need to define a `wpa_supplicant.conf` file for your particular wireless network. Put this file in the `boot` folder, and when the Pi first boots, it will copy that file into the correct location in the Linux root file system and use those settings to start up wireless networking. After the Pi is connected to power, make sure to wait a few (up to 5) minutes for it to boot up and register on the network. The Pi&#39;s IP address will not be visible immediately after power on, so this step is crucial to connect to it headlessly. Depending on the OS and editor you are creating this on, the file could have incorrect newlines or the wrong file extension so make sure you use an editor that accounts for this. Linux expects the line feed (LF) newline character. For more information, see this [Wikipedia article](https://en.wikipedia.org/wiki/Newline).

**`wpa_supplicant.conf` file example:**

```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=CA

network={
 ssid="<Name of your wireless LAN>"
 psk="<Password for your wireless LAN>"
}
```
Note that some older wireless dongles don&#39;t support 5GHz networks.

More information on the `wpa_supplicant.conf` file can be found [here](https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md).

### 1.1.3. Enable SSH Access

To enable ssh, you will need to create an empty file in the **`boot`** folder called **`ssh`**

### 1.1.4. Enable Serial Gadget Driver
As RPi Zero has one micro USB port. It is by default used to connect devices like a keyboard or a mouse through USB OTG. In our application, we want to use this usb port instead for serial communication with the computer. Accordingly, some settings need to be changed.

1. **USB Driver Setting**

Enable  **`dwc2`**  driver in  **`BOOT/config.txt`**, add the line at the end. At the same time you can enable/disable anything extra you might need like SPI or I2C.

```
dtoverlay=dwc2
```

2. **Modify default cmdline.txt to enable serial gadget driver**

We need to enable loading of the serial USB gadget driver.

In **`BOOT/cmdline.txt`**:

Add `modules-load=dwc2,g_serial` to the kernel command line file, `cmdline.txt` in `boot` and remove the `init=/usr/lib/raspi-config/init_resize.sh` part as otherwise the first boot will resize the root partition and the USB drivers won't engage until the next boot and it will first look like the configuration failed. Note the `root=PARTUUID=xxxxxxxx-yy` part, don't modify that.

## 1.2. Connect to your Board
First of all, insert the prepared micro SD card to the RPi. Use the USB cable to connect the Raspberry Pi to your computer. Make sure to connect to the port labelled **USB** NOT the one labelled **PWR**. After a few minutes, the Raspberry Pi should be running and you will need to confirm two things:

1. The Raspberry Pi is showing as a COM port. You can confirm that through the Device Manager in Windows.
2. The Raspberry Pi has connected successfully to your local wireless network and has obtained an IP Address. At this point, you should also note down the IP Address of the RPi.
To find the IP address, there are multiple ways. You can check the **Retrieving your Raspberry Pi’s IP Address from another device** section [here](https://pimylifeup.com/raspberry-pi-ip-address/) as an example.

## 1.3. Setup a method to transfer files to the Raspberry Pi
You will ned a way to transfer files from your computer to the Raspberry Pi. This will be mainly needed in order to copy the trained models files to the Raspberry Pi. There are multiple ways to do that such as copying files over SSH or setting up a samba server. However, we will go over only one method here that works for Windows.

1. Download WinSCP from [here](https://winscp.net/eng/index.php)
2. Install your favorite layout. I chose **Explorer**
3. When it opens setup the following in **Session**:
```
File Protocol: SCP
Host name: The IP address of you Raspberry Pi
User name: pi
Password: raspberry
```
4. **(This is Optional)** In **Advanced > SCP /Shell**:
```
Shell: sudo su – (if you want to be able to write to protected directories, e.g. /var/ww/ to transfer files for apache web server)
```
5. Connect and you can transfer files just by dragging and dropping.

### 1.4. Download Python 3 and the required dependencies
//TODO

### 1.5. Clone the python script

1. SSH to the raspberry pi using `ssh pi@<IP_ADDRESS>` and then enter the password, which is `raspberry` by default
2. Create a folder in the Raspberry Pi, let's create it in the home directory. First `cd ~` and then `mkdir SFU_ML` to create the directory
3. open the folder by `cd SFU_ML`
3. Initialize a repo through `git init`
4. Allow cloning subdirectories using `git config core.sparsecheckout true`
5. To choose the right folder to clone, use `echo 'RPi_Script*' >> .git/info/sparse-checkout`
6. Add the remote repo using `git remote add -f origin https://github.com/RamyE/SFU_ML.git`
7. Clone the folder using `git pull origin master`
8. Later when you want to get the latest updates from the repo, you can go to the folder and just use `git pull`

# 2. Set up and Run the GUI

## 2.1. Setup the Virtual Environment
//TODO
## 2.2. Clone the repo
//TODO
## 2.3. Run!
//TODO