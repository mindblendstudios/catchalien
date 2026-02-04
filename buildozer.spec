[app]

title = Catch An Alien
package.name = catchalien
package.domain = org.manisha

source.dir = .
source.include_exts = py,png,jpg,mp3

version = 1.0

requirements = python3,kivy,pyjnius

orientation = portrait
fullscreen = 1

android.ndk = 25b
android.api = 33
android.minapi = 23

# CRITICAL
android.archs = arm64-v8a

android.accept_sdk_license = True
android.skip_update = False
android.sdk = 34
android.build_tools_version = 34.0.0

android.enable_androidx = True
android.use_androidx = True

