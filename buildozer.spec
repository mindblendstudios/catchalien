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


android.sdk_path = /usr/local/lib/android/sdk
android.ndk_path = /usr/local/lib/android/sdk/ndk/25.2.9519653
android.ndk = 25b
android.api = 34
android.minapi = 23
android.skip_update = True
android.permissions = INTERNET

