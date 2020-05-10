# FileSigner
Prepend your signature to files created by you.
The signature is in form of your name and a timestamp of when the file was created

# How to use
> **Via the command line**
  - clone the repository `https://github.com/Harjacober/FileSigner.git`
  - change your current directory to the `FileSigner` directory then,
  - run `python signer.py --dir_path=[path to directory or file to be signed] --author=[name of the file owner]`
  - if specified `--dir_path` is a folder, it will sign all supported files in that folder. But if a file is specified, it will sign it if supported
> **Windows application**
 - Download the installer file at ``
 - once the .exe file is installed, the `FileSigner` application is automatically added to the registry file
 - To sign files in a folder, simply right click in the window of the current folder then click `Sign here` in the context menu that pops up to sign all files in that folder
 
***A file cannot be signed more than once. the scripts checks if a file has been signed before attempting to sign again***

# Note
> **Command Line Application**
  - Using the application via the command line allows you to sign a single file and all files in a folder
  - You have to specify the author name and directory path explicitly
> **Windows Application**
  - No need to specify the directory path or the author name. The name of the current user is automatically used to sign the file
  - Only files in a directory can be signed. Single file cannnot be signed
  
# Supported files
```
{py,java,js,c,php,kt,go,pl,rb,xml,cofee,css,html,dart}
```
