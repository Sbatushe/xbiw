# xbi
Xbps-install wrapper written in Python that doesn't care about case sensitiveness and package versions.

![xbi](https://raw.githubusercontent.com/Sbatushe/xbi/main/Istantanea_2021-11-12_13-31-56.png)

### Description
This Python script can be easily aliased and called using xi or xbi. This allows to easily install packets without worrying about software versions and case sensitiveness. This script is totally safe because it will launch xbps-install without the -y option.

### Configure
If you use sudo there's nothing to configure. If you use doas, edit the script and set the superuser value to doas

### Install
Just alias the script with something like xi or xbi
