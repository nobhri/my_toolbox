# command.sh

# https://docs.microsoft.com/ja-jp/windows/wsl/basic-commands

# show help
wsl --help

# set default version of WSL
# 1 or 2
wsl --set-default-version <Version>

# update WSL
wsl --update

# check status
wsl --status

# set version number to specific linux distribution
wsl --set-version <distribution name> <versionNumber>

# open with explorer
explorer.exe .