┌──(secretK㉿thebattle)-[~/picoCTF/reverse_engineering/unpackme]
└─$ upx -d unpackme-upx 
                       Ultimate Packer for eXecutables
                          Copyright (C) 1996 - 2024
UPX 4.2.2       Markus Oberhumer, Laszlo Molnar & John Reiser    Jan 3rd 2024

        File size         Ratio      Format      Name
   --------------------   ------   -----------   -----------
   1006445 <-    379188   37.68%   linux/amd64   unpackme-upx

Unpacked 1 file.
                                                                                                
┌──(secretK㉿thebattle)-[~/picoCTF/reverse_engineering/unpackme]
└─$ ls
unpackme-upx
                                                                                                
┌──(secretK㉿thebattle)-[~/picoCTF/reverse_engineering/unpackme]
└─$ subl README.md          






{
  long in_FS_OFFSET;
  int local_44;
  char *local_40;
  undefined8 local_38;
  undefined8 local_30;
  undefined8 local_28;
  undefined4 local_20;
  undefined2 local_1c;
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  local_38 = 0x4c75257240343a41;
  local_30 = 0x30623e306b6d4146;
  local_28 = 0x6865666430486637;
  local_20 = 0x36636433;
  local_1c = 0x4e;
  printf("What\'s my favorite number? ");
  __isoc99_scanf(&DAT_004b3020,&local_44);
  if (local_44 == 0xb83cb) {
    local_40 = (char *)rotate_encrypt(0,&local_38);
    fputs(local_40,(FILE *)stdout);
    putchar(10);
    free(local_40);
  }
  else {
    puts("Sorry, that\'s not it!");
  }
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return 0;
}



└─$ upx -d unpackme-upx
                       Ultimate Packer for eXecutables
                          Copyright (C) 1996 - 2024
UPX 4.2.2       Markus Oberhumer, Laszlo Molnar & John Reiser    Jan 3rd 2024

        File size         Ratio      Format      Name
   --------------------   ------   -----------   -----------
upx: unpackme-upx: NotPackedException: not packed by UPX

Unpacked 0 files.
                                                                                                                    
┌──(secretK㉿thebattle)-[~/picoCTF/reverse_engineering/unpackme]
└─$ ls    
unpackme-upx
                                                                                                                    
┌──(secretK㉿thebattle)-[~/picoCTF/reverse_engineering/unpackme]
└─$ chmod +x unpackme-upx
                                                                                                                    
┌──(secretK㉿thebattle)-[~/picoCTF/reverse_engineering/unpackme]
└─$ ls
unpackme-upx
                                                                                                                    
┌──(secretK㉿thebattle)-[~/picoCTF/reverse_engineering/unpackme]
└─$ ./unpackme-upx
What's my favorite number? 754635
picoCTF{up><_m3_f7w_5769b54e}



754635