#!/bin/bash

# Define your variables
dir="$HOME/.config/rofi/handy_stuff_menu"
theme='style'
scriptsDir="$HOME/.config/hypr/scripts"

# Rofi CMD
rofi_cmd() {
	rofi -dmenu \
		-p "Screen Capture" \
		-mesg "Select an option:" \
		-theme "${dir}/${theme}.rasi" <<EOF
󰈹


󰉋
EOF
}

# Check if "firefox" is running
is_firefox_running() {
	if hyprctl clients | grep -qi "class: firefox"; then
		return 0  # "firefox" is found (case-insensitive)
	else
		return 1  # "firefox" is not found
	fi
}

# Check if "thunar" is running (case-insensitive)
is_thunar_running() {
	if hyprctl clients | grep -qi "class: thunar"; then
		return 0  # "thunar" is found (case-insensitive)
	else
		return 1  # "thunar" is not found
	fi
}

# Check if "alacritty" is running (case-insensitive)
is_alacritty_running() {
	if hyprctl clients | grep -qi "class: alacritty"; then
		return 0  # "alacritty" is found (case-insensitive)
	else
		return 1  # "alacritty" is not found
	fi
}

# Check if "code" (VSCode) is running (case-insensitive)
is_vscode_running() {
	if hyprctl clients | grep -qi "class: code"; then
		return 0  # "code" is found (case-insensitive)
	else
		return 1  # "code" is not found
	fi
}

# Execute Command
run_cmd() {
	case "$1" in
		'󰈹')
			# Check if "firefox" is running
			if is_firefox_running; then
				hyprctl dispatch focuswindow firefox
			else
				firefox &>/dev/null &
			fi
			;;
		'')
			# Check if "alacritty" is running
			if is_alacritty_running; then
				hyprctl dispatch focuswindow Alacritty
			else
				alacritty &
			fi
			;;
		'󰉋')
			# Check if "thunar" is running
			if is_thunar_running; then
				hyprctl dispatch focuswindow Thunar
				hyprctl dispatch focuswindow thunar
			else
				thunar &
			fi
			;;
		'')
			# Check if "code" (VSCode) is running
			if is_vscode_running; then
				hyprctl dispatch focuswindow code-oss
			else
				code &
			fi
			;;
		*)
			exit 0
			;;
	esac
}

# Actions
chosen="$(rofi_cmd)"
run_cmd "$chosen"
