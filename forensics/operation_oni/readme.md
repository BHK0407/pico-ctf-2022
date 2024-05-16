┌──(secretK㉿thebattle)-[~/picoCTF/Forensics/operation_oni]
└─$ wget https://artifacts.picoctf.net/c/71/disk.img.gz
--2024-05-10 00:56:52--  https://artifacts.picoctf.net/c/71/disk.img.gz
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 108.157.38.128, 108.157.38.22, 108.157.38.100, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|108.157.38.128|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 48132743 (46M) [application/octet-stream]
Saving to: ‘disk.img.gz’

disk.img.gz             100%[==============================>]  45.90M  6.59MB/s    in 7.9s    

2024-05-10 00:57:01 (5.79 MB/s) - ‘disk.img.gz’ saved [48132743/48132743]

                                                                                               
┌──(secretK㉿thebattle)-[~/picoCTF/Forensics/operation_oni]
└─$ gunzip disk.img.gz     
                                                                                               
┌──(secretK㉿thebattle)-[~/picoCTF/Forensics/operation_oni]
└─$ ls -ltr
total 235524
-rw-r--r-- 1 secretK secretK 241172480 Aug  4  2023 disk.img


└─$ sudo autopsy        
[sudo] password for secretK: 

============================================================================

                       Autopsy Forensic Browser 
                  http://www.sleuthkit.org/autopsy/
                             ver 2.24 

============================================================================
Evidence Locker: /var/lib/autopsy
Start Time: Fri May 10 00:58:48 2024
Remote Host: localhost
Local Port: 9999

Open an HTML browser on the remote host and paste this URL in it:

    http://localhost:9999/autopsy

Keep this process running and use <ctrl-c> to exit








New Case


1. Case Name: The name of this investigation. It can contain only letters, numbers, and symbols.
  	
 
2. Description: An optional, one line description of this case.
  	
 
3. Investigator Names: The optional names (with no spaces) of the investigators for this case.
 	a. 
b. 
 	c. 
d. 
 	e. 
f. 
 	g. 
h. 
 	i. 
j. 


Create Case	
Cancel
Help



Do same types of the last autopsy we do before and look at "root" to find public and private key

-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW
QyNTUxOQAAACBgrXe4bKNhOzkCLWOmk4zDMimW9RVZngX51Y8h3BmKLAAAAJgxpYKDMaWC
gwAAAAtzc2gtZWQyNTUxOQAAACBgrXe4bKNhOzkCLWOmk4zDMimW9RVZngX51Y8h3BmKLA
AAAECItu0F8DIjWxTp+KeMDvX1lQwYtUvP2SfSVOfMOChxYGCtd7hso2E7OQItY6aTjMMy
KZb1FVmeBfnVjyHcGYosAAAADnJvb3RAbG9jYWxob3N0AQIDBAUGBw==
-----END OPENSSH PRIVATE KEY-----


" Carefule of that there is a blank line for this key"


ssh -i id_ed25519 -p 57553 ctf-player@saturn.picoctf.net


┌──(secretK㉿thebattle)-[~/picoCTF/Forensics/operation_oni]
└─$ ssh -i id_ed25519 -p 57553 ctf-player@saturn.picoctf.net 
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@         WARNING: UNPROTECTED PRIVATE KEY FILE!          @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Permissions 0644 for 'id_ed25519' are too open.
It is required that your private key files are NOT accessible by others.
This private key will be ignored.
Load key "id_ed25519": bad permissions
ctf-player@saturn.picoctf.net's password: 

                                                                                               
┌──(secretK㉿thebattle)-[~/picoCTF/Forensics/operation_oni]
└─$ ls -la
total 235536
drwxr-xr-x  2 secretK secretK      4096 May 10 01:17 .
drwxr-xr-x 11 secretK secretK      4096 May 10 00:56 ..
-rw-r--r--  1 secretK secretK 241172480 Aug  4  2023 disk.img
-rw-r--r--  1 secretK secretK       410 May 10 01:17 id_ed25519
                                                                                               
┌──(secretK㉿thebattle)-[~/picoCTF/Forensics/operation_oni]
└─$ chmod 600 id_ed25519
                                                                                               
┌──(secretK㉿thebattle)-[~/picoCTF/Forensics/operation_oni]
└─$ ssh -i id_ed25519 -p 57553 ctf-player@saturn.picoctf.net
Load key "id_ed25519": error in libcrypto
ctf-player@saturn.picoctf.net's password: 

                                                                                                
┌──(secretK㉿thebattle)-[~/picoCTF/Forensics/operation_oni]
└─$ ls -la                                                  
total 235536
drwxr-xr-x  2 secretK secretK      4096 May 10 01:17 .
drwxr-xr-x 11 secretK secretK      4096 May 10 00:56 ..
-rw-r--r--  1 secretK secretK 241172480 Aug  4  2023 disk.img
-rw-------  1 secretK secretK       410 May 10 01:17 id_ed25519
                                                                                                
┌──(secretK㉿thebattle)-[~/picoCTF/Forensics/operation_oni]
└─$ 


┌──(secretK㉿thebattle)-[~/picoCTF/Forensics/operation_oni]
└─$ ssh -i id_ed25519 -p 57553 ctf-player@saturn.picoctf.net
Welcome to Ubuntu 20.04.5 LTS (GNU/Linux 6.5.0-1016-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

This system has been minimized by removing packages and content that are
not required on a system that users do not log into.

To restore this content, you can run the 'unminimize' command.

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

ctf-player@challenge:~$ 

ctf-player@challenge:~$ ls
flag.txt
ctf-player@challenge:~$ cat flag.txt
picoCTF{k3y_5l3u7h_af277f77}
ctf-player@challenge:~$ 



