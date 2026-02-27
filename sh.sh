printf "\033c\033[40;37m\n\n"
sudo debootstrap stable ./ http://deb.debian.org/debian
tree ./
#if you system is other change this
sudo chroot ./ /bin/sh

