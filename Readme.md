#### DEPRECATED, please use the most up to date project https://github.com/salvadormrf/vagrant-gae-wagtail

### Run wagtail with Google App Engine SDK
```
# create virtualenv for local development
mkvirtualenv wagtail_gae
pip install -r dev-requirements.txt --allow-external PIL --allow-unverified PIL

# download external dependencies
pip install -r gae-requirements.txt -t lib/

# create mysql database (Mysql 5.5)
mysql -uroot -p
CREATE DATABASE `wagtail_gae_demo` CHARACTER SET utf8 COLLATE utf8_general_ci;

# run migrations
python manage.py migrate

# run collectstatic
python manage.py compress
python manage.py collectstatic

# run development server
dev_appserver.py .
```

#### Make sure you have PIL installed on your system with JPEG, ZLIB and FREETYPE2 support.
```
# sudo ln -s /usr/local/include/freetype2 /usr/local/include/freetype
# sudo ln -s /usr/include/freetype2 /usr/include/freetype2/freetype

# ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib
# ln -s /usr/lib/x86_64-linux-gnu/libfreetype.so /usr/lib
# ln -s /usr/lib/x86_64-linux-gnu/libz.so /usr/lib
```

```
    --------------------------------------------------------------------
    PIL 1.1.7 SETUP SUMMARY
    --------------------------------------------------------------------
    version       1.1.7
    platform      linux2 2.7.5+ (default, Feb 27 2014, 19:37:08)
                  [GCC 4.8.1]
    --------------------------------------------------------------------
    *** TKINTER support not available (Tcl/Tk 8.6 libraries needed)
    --- JPEG support available
    --- ZLIB (PNG/ZIP) support available
    --- FREETYPE2 support available
    *** LITTLECMS support not available
    --------------------------------------------------------------------
```

#### Add write permissions on bucket for appengine
```
sudo apt-get install libffi-dev
pip install gsutil

gsutil -m acl ch -r -u user@appspot.gserviceaccount.com:W gs://mybucket
```
