# Hyprland Dots

My dotfiles

## Dependencies
- swaybg (for setting wallpaper)
- rofi-lbonn-wayland
- eww-wayland (available in AUR)
  - Eww is better than waybar in my opinion. It uses fewer system resources and looks better.
- swaync (notification daemon, it's really cool :))
- ![image](https://github.com/Asif-Tanvir-2006/hyprland_dots/assets/98411318/02af7aa7-ed60-44f9-8fc2-4696da7d39b0)
- mpris (media player widget for swaync)
- i3status-rust-git (for the volume progress bar)
  - Also note that I am using amixer, which is what the volume info that appears at the top right corner of your monitor (you can see in the preview below) is supposed to work with.
- ![Untitled](https://github.com/Asif-Tanvir-2006/hyprland_dots/assets/98411318/b6b22030-560e-4dbc-b5f0-fc18d4ed9ab1)

## Optional (but I recommend you download them, will really make life easier for you)
- grimblast (screenshot and stuff)
- clipman (for clipboard history)
- gammastep (night light, available in AUR)

## Keybinds
- `mod + V` = Access your clipboard
  - ![image](https://github.com/Asif-Tanvir-2006/hyprland_dots/assets/98411318/faf79cd4-8ee8-4a40-b3a3-18ad5b99f882)

- `mod + shift + D` = Access folders (I am using thunar, if you use any other file manager, make changes to `~/.config/hypr/scripts/folders_rofi.sh` accordingly)
  - ![image](https://github.com/Asif-Tanvir-2006/hyprland_dots/assets/98411318/23f856fb-c7a0-49e9-af68-d1bd4539353d)

- `mod + D` = Launch rofi
  - ![image](https://github.com/Asif-Tanvir-2006/hyprland_dots/assets/98411318/5ef78958-7f54-4ebf-b7e9-ca2c94e90526)


- `shift + print` = Save screenshot
- `print` = Copy screenshot to clipboard
- `mod + N` = Toggle swaync notification pane
- `mod + O` = Organise your home directory (scans directories and puts files in respective folders, check hypr/scripts/organiser.sh for details)

Go through my config files for detailed information on all the keybinds I use. You can obviously change them as per your needs.
## Important ly note (login manager)
The config folder is /etc/ly
In the config.ini, I have set bg=0, that prevents it from flashing a temporary white screen in the time that takes to load hyprland.
