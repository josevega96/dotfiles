#! /bin/sh
##
#script for restoring debian packages
##

sudo apt install gnupg
sudo apt-key add Repo.keys
sudo cp -R sources.list* /etc/apt/
sudo apt-get update
sudo apt-get install dselect -y
sudo dselect update
sudo dpkg --set-selections < Package.list && sudo apt-get dselect-upgrade -y
