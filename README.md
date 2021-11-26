# XBIW
xbiw (XBps-Install Wrapper) is a xbps-install wrapper written in Python and it doesn't care about case sensitiveness or package versions.

![xbiw](https://raw.githubusercontent.com/Sbatushe/xbi/main/sample.png)

### Description
This wrapper allows to easily install packages without worrying about software versions and case sensitiveness. This script is totally safe because it will launch xbps-install without the -y option.

### Configure
If you want to change your superuser value, you can modify the `/usr/bin/xbiw` file and add `sudo` or `doas` where specified

### FAQ
Q: What will happen if you install a package with different versions?

A: Nothing, because the script can accept only 1 possible version. If versions are more or less, it stops. If you need to install some strange type of software version, just use xbps-install. However, it's very unlikely that you will find a software with different versions.
