tcpflow -r capture.flag.pcap 

└─$ openssl des3 -d -salt -in file.des3 -out file.txt -k supersecretpassword123


                                                                                               
┌──(secretK㉿thebattle)-[~/picoCTF/Forensics/eavesdrop]
└─$ file 010.000.002.015.56370-010.000.002.004.09002                           
010.000.002.015.56370-010.000.002.004.09002: openssl enc'd data with salted password
                                                                                               
┌──(secretK㉿thebattle)-[~/picoCTF/Forensics/eavesdrop]
└─$ file *                                          
010.000.002.004.09001-010.000.002.015.57876:   ASCII text
010.000.002.015.43928-035.224.170.084.00080:   ASCII text, with CRLF line terminators
010.000.002.015.56370-010.000.002.004.09002:   openssl enc'd data with salted password
010.000.002.015.57876-010.000.002.004.09001:   ASCII text
035.224.170.084.00080-010.000.002.015.43928:   ASCII text, with CRLF line terminators
035.224.170.084.00080-010.000.002.015.43928c1: data
capture.flag.pcap:                             pcap capture file, microsecond ts (little-endian) - version 2.4 (Ethernet, capture length 262144)
file.des3:                                     openssl enc'd data with salted password
file.txt:                                      ASCII text, with no line terminators
report.xml:                                    XML 1.0 document, ASCII text, with very long lines (743)
                       



picoCTF{nc_73115_411_dd54ab67}