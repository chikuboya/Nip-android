[app]
title = Nip
package.name = nip
package.domain = org.chikuboya
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttc
version = 0.1
icon.filename = %(source.dir)s/icon.png

# ★ kivmob, android, pyjnius を追加
requirements = python3,kivy==2.3.0,pillow,android,pyjnius,kivmob

orientation = portrait
fullscreen = 1

# ★ 広告通信用の権限を追加
android.permissions = INTERNET, ACCESS_NETWORK_STATE

android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21

# ★ AdMobアプリIDの設定
android.meta_data = com.google.android.gms.ads.APPLICATION_ID=ca-app-pub-3649897440139100~8105670662

log_level = 2

[buildozer]
log_level = 2
warn_on_root = 1
