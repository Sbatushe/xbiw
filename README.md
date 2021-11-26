# XBIW
xbiw (XBps-Install Wrapper) is a xbps-install wrapper written in Python and it doesn't care about case sensitiveness or package versions.

![xbiw](https://raw.githubusercontent.com/Sbatushe/xbi/main/sample.png)

### Description
This wrapper allows to easily install packages without worrying about software versions and case sensitiveness. This script is totally safe because it will launch xbps-install without the -y option.

### Configure
If you want to change your superuser value, you can modify the script and add `sudo` or `doas` where specified

### Installation
Clone the repository:
```
git clone https://github.com/Sbatushe/xbiw
```
Install:
```
cp xbiw/xbiw /usr/bin
```

### FAQ
Q: What will happen if you install a package with different versions?

A: This is unlikely to happen (such packages doesn't exist), but if it does, the script won't install nothing: the script can accept only 1 possible version. If the script is unsure about the package to install it won't install nothing (and you could open an issue).
