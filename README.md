MiaoVideoServer is a server based on django. It provides a convinent way for one who wants to watch his PC's videos on their phones using browser instead of extra player--like oplayer.( however I have to admit that it is well-design and rather powerful.)  


>prerequesite
-Django 2.0
-python3

>HOW TO USE IT
-change the MEDIA_ROOT (setting.py) to the path where your video located 
-add your LAN IP address (both host and client) to the ALLOWED_HOSTS (setting.py)
-change the firewall to open the port (both in and out)
-run the surver 
    python manage.py runserver 0.0.0.0:8000 (or whatever port you like)

>WHAT HAVE BEEN DONE
-a usable and simple video server for android and windows (YES IOS is not include)

>TO DO NEXT
-authentication
-support more video format
-IOS compatibility 

>xia mian mei you le
