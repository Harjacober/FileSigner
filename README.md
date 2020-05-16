# FileSigner
Helps prepend your signature to files created by you.
The signature is in form of your name and a timestamp of when the file was created. See screenshots at the end for how a signed file looks like.

# How to use
> **Via the command line**
  - clone the repository [here](https://github.com/Harjacober/FileSigner.git)
  - change your current directory to the `FileSigner` directory then,
  - run `python main.py --dir_path=[path to directory or file to be signed] --author=[name of the file owner]`
  - if specified `--dir_path` is a folder, it will sign all supported files in that folder. But if a file is specified, it will sign it if supported
> **Windows application**
 - Download the installer file [here](https://drive.google.com/file/d/1u_6giH7OpeyLJCgA5sAn3gN6nTm8MUos/view?usp=sharing)
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
  
# Supported files types
```
{py,java,js,c,php,kt,go,pl,rb,xml,cofee,css,html,dart}
```

# How to contribute
- To improve the windows application, look inside the app folder
- To improve the command line application, simply look at the `main.py` file
- To test your implementation, look inside the test folder and write test for your new implementation in the `test.py` file
  **Contribution ideas**
    - implement an optimal algorithm to check if a file has already been signed before
    - Allow the window application to support signing of a single file
    - Add support for more file types
    - Add support for files that doesn't support multi-line comments. e.g `R files`

# Sample
![alt text](https://github.com/Harjacober/FileSigner/blob/master/test/images/java.png)  ![alt text](https://github.com/Harjacober/FileSigner/blob/master/test/images/python.png)
