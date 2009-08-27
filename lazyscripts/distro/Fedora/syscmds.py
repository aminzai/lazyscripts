#!/usr/bin/env python
"""
Here store the command which only in Fedora
"""
import os

detect_pack = "rpm -q "
install_cmd = "yum -y install "
remove_cmd = "yum -y remove "
refresh_cmd = "yum check-update"
network_config = "nm-connection-editor"

if os.getenvp['WIN_MGR']:
    win_mgr = os.getenv('WIN_MGR')
else:
    win_mgr = ""

if win_mgr == 'Gnome':
#    repo_config = "sudo -u %s 'gpk-repo'" % (os.getenv('REAL_USER')) 
    repo_config = "gpk-repo"
elif win_mgr == 'KDE':
    repo_config = "kpackagekit --settings"
else:
#    repo_config = "sudo -u %s 'gpk-repo'" % (os.getenv('REAL_USER')) 
    repo_config = "gpk-repo"

# Fedora 8: repo_config = "python /usr/lib/python2.5/site-packages/pirut/RepoSelector.py"


if __name__ == "__main__" :
    print detect_pack
    print install_cmd
    print remove_cmd
    print refresh_cmd
    print network_config
    print repo_config

