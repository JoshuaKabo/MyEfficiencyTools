xremap /home/joshk/MyDevStuff/MyEfficiencyTools/FullyCustom_xremap.yml --device /dev/input/event4
# How to use:
# Install xremap
# Install crontab (whatever flavor, EOS seems to use cronie (yay cron, get cronie))
# Activate crontab using systemctl
    # Just because it's installed doesn't mean it's active
    # sudo systemctl enable cronie
    # sudo systemctl start cronie
# use "crontab -e" to make an entry for "@reboot /home/joshk/MyDevStuff/MyEfficiencyTools/BootCronScript.sh"
