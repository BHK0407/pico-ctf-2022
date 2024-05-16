get the file from web site

---> disk.flag.img.gz

then extract the file with gunzip

gunzup disk.flag.img.gz

---> disk.flag.img

sudo autopsy

open port 9999


http://localhost:9999/autopsy


--->new case


--->
Add host
--->
Add Img
---> Search for real path

/home/kali/picoCTF/Forensics/sleuthkit_apprentice/disk.flag.img


After that choose analyze this file: 	disk.flag.img-360448-614399

---> analyze ---> File analysis


file the folder: "my_folder"

and we will see those files of the flag

The download the flag.uni.txt (remember after that moving it to flag.uni.txt)

then use cat to read

===> picoCTF{by73_5urf3r_2f22df38}