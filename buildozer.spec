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

# CRITICAL
android.archs = arm64-v8a, armeabi-v7a

android.permissions = INTERNET
