---
title: "Arch Install and Initial Config"
date: 2020-07-12T21:22:01+02:00
draft: true 
---

![ScreenShot](/image/arch_screenshot.png)
1.      Connect to internet
        ip link :       For ethernet connection.
        iwctl   :       For wifi connection.

2.      Clear/Format disk
        fdisk /dev/sda
        g create new gpt label
        p print the partition table
        n create a new partition
        d delete a partition
        q quit without saving changes
        w write the new partition table and exit

3.      Format disk type
        mkfs.fat -F32   /dev/sda1
        mkfs.ext4       /dev/sda2

4.      Mounting and file Structure
        mount /dev/sda2 /mnt
        mkdir -p /mnt/{home,data,etc}
        mount /dev/sdb1 /mnt/data

5.      genfstab -U -p /mnt >> /mnt/etc/fstab

6.      pacstrap -i /mnt base

7.      arch-chroot /mnt

8.      pacman -S linux-lts linux-lts-headers base-devel linux-firmware vim networkmanager wpa_supplicant wireless_tools netctl dialog nvidia-lts nvidia-utils grub efibootmgr os-prober mtools dosfstools intel-ucode xorg-server xorg neofetch plasma-desktop plasma-meta gimp termite dolphin git vlc vifm i3

9.      ln -sf /usr/share/zoneinfo/Africa/Windhoek > /etc/localtime
        hwclock --systohc

10.     vim /etc/locale.gen
        locale-gen
        vim /etc/locale.conf
        LANG=en_US.UTF-8

11.     mkinitcpio -p linux-lts

12.     useradd -m -g users -G wheel nihar
        passwd
        passwd nihar

13.     visudo
        enable wheels

14.     GRUB UEFI
        mkdir /boot/efi
        mount /dev/sda1 /boot/efi
        grub-install --target=x86_64-efi --bootloader-id=grub --recheck
        ls -lart /boot/grub/locale/en*mo

8.      pacman -S linux-lts linux-lts-headers base-devel linux-firmware vim networkmanager wpa_supplicant wireless_tools netctl dialog nvidia-lts nvidia-utils grub efibootmgr os-prober mtools dosfstools intel-ucode xorg-server xorg neofetch plasma-desktop plasma-meta gimp termite dolphin git vlc vifm i3

9.      ln -sf /usr/share/zoneinfo/Africa/Windhoek > /etc/localtime
        hwclock --systohc

10.     vim /etc/locale.gen
        locale-gen
        vim /etc/locale.conf
        LANG=en_US.UTF-8

11.     mkinitcpio -p linux-lts

12.     useradd -m -g users -G wheel nihar
        passwd
        passwd nihar

13.     visudo
        enable wheels

14.     GRUB UEFI
        mkdir /boot/efi
        mount /dev/sda1 /boot/efi
        grub-install --target=x86_64-efi --bootloader-id=grub --recheck
        ls -lart /boot/grub/locale/en*mo

22.     swapfile
        fallocate -l 2G /swapfile
        chmod 600 /swapfile
        mkswap /swapfile
        echo "/swapfile none swap sw 0 0' | tee -a /etc/fstab

23. vim /etc/hostname
        predator

24. vim /etc/hosts
        127.0.0.1       localhost
        ::1             localhost
        127.0.1.1       predator.localdomain    predator

25.     systemctl enable NetworkManager

----reboot----

26. nmcli device wifi list
        nmcli device wifi connect SSID password "password"

27.     vim /etc/pacman.d/conf
        enable multilib
        ILoveCandy
        uncomment

28. git clone https://aur.archlinux.org/yay.git
        yay git
        makepkg -si

29. Install additional software
        yay -S brave optimus-manager optimus-manager-qt

