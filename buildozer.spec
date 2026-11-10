[app]
title = Configurador FF
package.name = configuradorff
package.domain = org.exemplo
source.dir = .
source.include_exts = py,json
version = 1.0
requirements = python3,kivy==2.3.1
orientation = portrait
fullscreen = 0

android.api = 35
android.minapi = 23
android.archs = arm64-v8a
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
