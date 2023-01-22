# armbian-orange-pi-5-ansible
## About
This is a collection of ansible roles that I use for [Orange Pi 5 SBC](http://www.orangepi.org/html/hardWare/computerAndMicrocontrollers/details/Orange-Pi-5.html)  running [Armbian Linux](https://www.armbian.com/orangepi-5/).
Since Orange Pi 5 is under heavy development and it is WIP/bleeding edge, then re-installing the OS to test latest builds became tedious and needed to be automated.

**Use at your own risk. I am not responsible for any damage resulting in the usage of this repository.**

If you want to help create a fork, PR or issue if you wish.
I am doing this as a hobby, so don't have too high excpectations.




## Prequesites
* Install [Orange Pi 5 jammy/legacy/minimal armbian linux from trunk builds](https://github.com/armbian/build/releases)
* Complete the first boot setup of armbian (set your root password, normal user with password, build locale, network connection etc...)
* Have SSH access to Your orange Pi 5 SBC or keyboard and screen connected to it
* *I have not tested with xfce image, but I think it should work too*

## Installation and usage
### Option 1: Running ansible from the SBC locally
```
#Login to your SBC over SSH or use it's keyboard and screen directly on the device
ssh <your regular user>@<Your Orange Pi 5 IP address>

#Install needed tools to use ansible, git and vim(you can use nano or something else too)
sudo apt install -y git ansible vim

#Clone this repo and go to it's directory
git clone https://github.com/martivo/armbian-orange-pi-5-ansible.git
cd armbian-orange-pi-5-ansible

#Create configuration files
cp site.example.yml site.yml
cp inventory.example-local.yml inventory.yml

#Edit site.yml to your needs. Read **About roles and variables** below for more info.
vim site.yml

#Edit inventory.yml to fit your setup. Read **About roles and variables** below for more info.
vim inventory.yml


#Run ansible
ansible-playbook site.yml

#Optional, reboot the SBC
```

### Option 2: Running ansible from another host to configure the SBC
```
#Install needed tools to use ansible and git
sudo apt install -y git ansible

#Clone this repo and go to it's directory
git clone https://github.com/martivo/armbian-orange-pi-5-ansible.git
cd armbian-orange-pi-5-ansible

#Create configuration files
cp site.example.yml site.yml
cp inventory.example-remote.yml inventory.yml

#Edit site.yml to your needs. Read **About roles and variables** below for more info.
vim site.yml

#Edit inventory.yml to fit your setup. Read **About roles and variables** below for more info.
vim inventory.yml

#Run ansible, if you have public key authentication in SSH then you can skip the --ask-pass flag.
ansible-playbook --ask-pass site.yml

#Optional, reboot the SBC
```

* If the roles purpose is unclear, then check what they do from the source code
* Some roles are dependnet on others, see **About roles and variables**
* _I have not created hooks, since a "reboot" after the play is expected_


## About roles and variables

| Role | Comment | Needed variables | Depends on role |
| --- | --- | --- | --- |
| disable-root-account | Lock root user and deny root ssh  | | |
| docker | Install Docker CE | | |
| extra-software | Additional pacakges that I like (transmission-gtk, vim, prometheus-node-exporter, armbian-config) | | |
| firefox-no-snap | Install firefox without using snap. | | |
| gdm-auto-login | Passwordless login for normal_user in GDM3 | normal_user | ubuntu-desktop-minimal | 
| gdm-enable-wayland | Enable wayland in GDM3 | | ubuntu-desktop-minimal, orangepi5-hdmi |
| [input-remapper](https://github.com/sezanzeb/input-remapper) | Software that enables to remap keys and mouse buttons | | |
| kodi | Installs kodi. [More...](https://forum.armbian.com/topic/25957-guide-kodi-on-orange-pi-5-with-gpu-hardware-acceleration-and-hdmi-audio/) |  |  gdm-enable-wayland |
| lgtv | Installs [LGWebOSRemote](https://github.com/klattimer/LGWebOSRemote) with configuration and some example scripts | lgtv_configuration, normal_user | |
| net-disable-ipv6 | Disable IPv6 | | |
| set-hostname | Set hostname for your Orange Pi 5  | hostname | |
| set-timezone | Set timezone for the host | timezone | |
| no-boot-logo | Disable bootloader logo to see verbose messages (minimal image has it already disabled) | | |
| no-swap | Disable swap  | | |
| orangepi5-hdmi | Install mesa drivers and configure hdmi sound. [More...](https://forum.armbian.com/topic/25957-guide-kodi-on-orange-pi-5-with-gpu-hardware-acceleration-and-hdmi-audio/) | | |
| sshfs | Mount SSHFS folder from another server. Creates a ssh keypair under /root/.ssh/sshfs that is used for the sshfs | ssh_fs_mount_connection,  ssh_fs_mount_directory | |
| surround-sound-test | Downloads a surround sound testing video to /home/{{ normal_user }}/ChID-BLITS-EBU.mp4 | normal_user | |
| ubuntu-desktop-minimal | Install ubuntu desktop minimal with a few addiditonal tools | | |
| user-ssh-authorized-key | Add a public ssh key to /home/{{ normal_user }}/.ssh/authorized_keys for passwordless login | normal_user,  user_ssh_authorized_key | |



Useful links:
https://forum.armbian.com/forum/206-orange-pi-5/ 
https://github.com/armbian/build/releases
