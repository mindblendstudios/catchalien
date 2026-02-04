[app]
title = Catch An Alien
package.name = catchalien
package.domain = org.manisha

source.dir = .
source.include_exts = py,png,jpg,mp3,kv

version = 1.0.0

requirements = python3==3.10,kivy

orientation = portrait
fullscreen = 1

# Android configuration
android.api = 34
android.minapi = 23
android.ndk = 25b
android.ndk_api = 23

android.permissions = INTERNET
android.skip_update = True

# Avoid legacy pyjnius issues
android.use_legacy_python = 0

# Performance / stability
android.archs = arm64-v8a
android.allow_backup = True
android.gradle_dependencies = androidx.core:core:1.12.0

# Build output
android.debug = 0
