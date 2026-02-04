[app]
title = Catch An Alien
package.name = catchalien
package.domain = org.manisha

source.dir = .
source.include_exts = py,png,jpg,mp3

version = 1.0

requirements = python3,kivy

orientation = portrait
fullscreen = 1

android.permissions = INTERNET
android.skip_update = True

# Android configuration
android.api = 34
android.minapi = 21
android.ndk = 25b

# CRITICAL — forces Buildozer to download build-tools (with aidl)
android.build_tools_version = 34.0.0

# Required new syntax
android.archs = arm64-v8a, armeabi-v7a

# Prevent Buildozer guessing paths
android.sdk_path =
android.ndk_path =


