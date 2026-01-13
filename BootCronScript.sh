xremap /home/joshk/dev/MyEfficiencyTools/FullyCustom_xremap.yml --device /dev/input/event4
# How to use:
# Install xremap
# Install crontab (whatever flavor, EOS seems to use cronie (yay cron, get cronie))
# Activate crontab using sysctl
    # Just because it's installed doesn't mean it's active
# use "sudo crontab -e" to make an entry for "@reboot /home/joshk/dev/MyEfficiencyTools/BootCronScript.sh"
