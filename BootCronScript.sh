bash xremap /home/joshk/Projects/MyEfficiencyTools/FullyCustom_xremap.yml --device /dev/input/event4
# How to use:
# Install xremap
# Install crontab (whatever flavor, EOS seems to use cronie (yay cron, get cronie))
# Activate crontab using systemctl
    # Just because it's installed doesn't mean it's active
    # sudo systemctl enable cronie
    # sudo systemctl start cronie
# use "sudo EDITOR=nano crontab -e" to make an entry for "@reboot /home/joshk/Projects/MyEfficiencyTools/BootCronScript.sh"
# add write permissions to this file by sudo chmod +x BootCronScript.sh
