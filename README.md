dotfiles from my personal setup
==================================

## Dependencies 
before trying to clone the repo please install the needed dependencies 


Arch repo:
python-pywal
rofi
kitty
dunst
firefox
ranger
code
alsa
pacmixer
backlight-git 
acpilight
python-i3ipc
lxsession

AUR:
polybar
compton-tryone-git
nerd-fonts-complete
ttf-google-sans
ms-office-online
whatsapp-nativefier-dark
telegram-desktop
spotify

External:

rofi-menus
https://gitlab.com/vahnrr/rofi-menus

minimal firefox 
https://github.com/mut-ex/minimal-functional-fox

wal vscode
https://marketplace.visualstudio.com/items?itemName=cmschuetz12.wal

oh my zsh 
https://ohmyz.sh/

## How to install 
I made this as a bare git repository so you can be able to clone directly to your home directory for mor info you can check 
https://www.atlassian.com/git/tutorials/dotfiles

steps 

1. set your alias in either your .zshrc o .bashrc 

```
alias config='/usr/bin/git --git-dir=$HOME/.cfg/ --work-tree=$HOME'
```

2. Add .cfg folder to .gitignore

```
echo ".cfg" >> .gitignore
```

3. Clone the bare git repository 

```
git clone --bare -b master https://github.com/josevega96/dotfiles $HOME/.cfg
```

4.Cloning might change the alias in your .bashrc or .zshrc if thats the case re add it 

```
alias config='/usr/bin/git --git-dir=$HOME/.cfg/ --work-tree=$HOME'
```

5.Checkout the current config 

```
config checkout
```
after checking out you might find some errors because the file already exists, if thats the case you can back it up if you have anything important or just delete it, after removing conflicting files checkout again

6.Set the flag showUntrackedFiles to no 

```
config config --local status.showUntrackedFiles no
```

7. Copy the fonts inside the .config/polybar/fonts

```
# cp ~/.config/polybar/fonts/* /usr/share/fonts
```

After all the steps are done all configs shound be installed and as an extra you should be able to use git for the config files installed in home directory 

## Screenshots

![screen shot of the finished setup](https://i.imgur.com/aIG77u7.jpg)
