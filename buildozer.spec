[app]
title = Catch An Alien
package.name = catchalien
package.domain = org.manisha

source.dir = .
source.include_exts = py,png,jpg,mp3

version = 1.0

requirements = python3==3.10,kivy,pyjnius==1.4.2

orientation = portrait
fullscreen = 1

android.api = 34
android.minapi = 23
android.ndk = 25b

android.permissions = INTERNET

android.skip_update = True
android.use_legacy_python = 1

- name: Set up Java 17
  uses: actions/setup-java@v4
  with:
    distribution: 'temurin'
    java-version: '17'
