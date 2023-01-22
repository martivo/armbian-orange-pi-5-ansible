# armbian-orange-pi-5-ansible
## About
This is a collection of ansible roles that I use for [Orange Pi 5 SBC](http://www.orangepi.org/html/hardWare/computerAndMicrocontrollers/details/Orange-Pi-5.html)  running [Armbian Linux](https://www.armbian.com/orangepi-5/).
Since Orange Pi 5 is under heavy development and it is WIP/bleeding edge, then re-installing the OS to test latest builds became tedious and needed to be automated.

**Use at your own risk. I am not responsible for any damage resulting in the usage of this repository.**

If you want to help create a fork, PR or issue if you wish.
I am doing this as a hobby, so don't have too high excpectations.




## Prequesites
Install [Orange Pi 5 jammy/legacy/minimal armbian linux from trunk builds](https://github.com/armbian/build/releases)
Complete the first boot setup of armbian (set your root password, normal user with password, build locale, network connection etc...)

* I have not tested with xfce image, but I think it should work too

## Installation
```
apt install -y git ansible
git clone https://github.com/martivo/armbian-orange-pi-5-ansible.git
cd armbian-orange-pi-5-ansible
cp site.yml.example site.yml
```

Edit site.yml variables and enable or disable desired roles. See role information below.

* These roles have only been tested with local execution, not over ssh
* If the roles purpose is unclear, then check what they do
* Some roles are dependnet on others
* I have not created hooks, since a "reboot" after the running is expected

## Running
```
ansible-playbook --ask-become-pass site.yml
reboot
```

About roles:
disable-root-account - removed root password and does not allow root to ssh into the machine. No variables.
docker - installs Docker CE
extra-software - Additional pacakges that I like (transmission-gtk, vim, prometheus-node-exporter, armbian-config)
firefox-no-snap - Install firefox without using snap.
gdm-auto-login - enable automatic GDM3 login for the "normal_user" variable (depends on ubuntu-desktop-minimal role)
gdm-enable-wayland - enable wayland for GDM3 (depends on ubuntu-desktop-minimal role)
input-remapper - software that enables to remap keys and mouse buttons
lgtv - Installs https://github.com/klattimer/LGWebOSRemote with configuration and some example scripts (needs "lgtv_configuration" and "normal_user" variable)
net-disable-ipv6 - Disable IPv6
net-set-hostname - Set hostname for your Orange Pi 5 
no-boot-logo - Disable bootloader logo to see verbose messages (minimal image has it already disabled)
no-swap - Disable swap 
orangepi5-hdmi - Install mesa drivers and configure hdmi sound (see https://forum.armbian.com/topic/25957-guide-kodi-on-orange-pi-5-with-gpu-hardware-acceleration-and-hdmi-audio/)
set-timezone - Set timezone for the host
sshfs - Mount SSHFS folder from another server. This also creates a ssh keypair under /root/.ssh/sshfs that you need to add to your remote server
surround-sound-test - Downloads a surround sound testing video to /home/{{ normal_user }}/ChID-BLITS-EBU.mp4
ubuntu-desktop-minimal - install ubuntu desktop minimal with a few addiditonal tools
user-ssh-authorized-key - add a public ssh key to /home/{{ normal_user }}/.ssh/authorized_keys for passwordless login. Needs "user_ssh_authorized_key" variable.


Useful links:
https://forum.armbian.com/forum/206-orange-pi-5/ 
https://github.com/armbian/build/releases
