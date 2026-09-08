# How to use:
# Install xremap
# If you installed using rustup & cargo, you need to add ~/.cargo/bin to ~/.profile or ~/.bashrc (or whatever shell in use)
# Install crontab (whatever flavor, EOS seems to use cronie (yay cron, get cronie))
# Activate crontab using systemctl
    # Just because it's installed doesn't mean it's active
    # sudo systemctl enable cronie
    # sudo systemctl start cronie
# use "sudo EDITOR=nano crontab -e" to make an entry for "@reboot /home/joshk/Projects/MyEfficiencyTools/BootCronScript.sh"
# add write permissions to this file by sudo chmod +x BootCronScript.sh
# Be sure the permissions include minimum of wrx,rx,rx for both yml and .sh

# Xremap automatically grabs keyboards. Also --watch makes it catch any keyboards you plug in, at any time.
/home/joshk/.cargo/bin/xremap --watch /home/joshk/Projects/MyEfficiencyTools/FullyCustom_xremap.yml