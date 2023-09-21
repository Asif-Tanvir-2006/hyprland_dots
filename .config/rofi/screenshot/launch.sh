
dir="~/.config/rofi/screenshot"
theme='style'
scriptsDir="$HOME/.config/hypr/scripts"
# Rofi CMD
rofi_cmd() {
	rofi -dmenu \
		-p "Screen Capture" \
		-mesg "Select an option:" \
		-theme ${dir}/${theme}.rasi <<EOF
󰹑


EOF
}

# Execute Command
run_cmd() {
	case "$1" in
		'󰹑')
			sleep 0.5 && grimblast --notify save screen ~/screenshot.png && ${scriptsDir}/ss_sorter.sh

			;;
		'')
			grimblast --notify copy area
			;;
		'')
			grimblast --notify save area screenshot.png && ${scriptsDir}/ss_sorter.sh
			;;
	
		*)
			exit 0
			;;
	esac
}

# Actions
chosen="$(rofi_cmd)"
run_cmd "$chosen"
