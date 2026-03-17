[app]

title = Nip
package.name = nip
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv,ttc

version = 1.0

icon.filename = icon.png

requirements = python3,kivy,pyjnius

orientation = portrait

fullscreen = 0

# 権限
android.permissions = INTERNET,ACCESS_NETWORK_STATE

# AdMob（超重要）
android.gradle_dependencies = com.google.android.gms:play-services-ads:22.6.0

# Android設定
android.api = 33
android.minapi = 21
android.ndk = 25b

# 起動
entrypoint = main.py

# ログ
log_level = 2

# ビルド高速化（おすすめ）
p4a.branch = master

# 画面回転防止
android.orientation = portrait

# デバッグ時便利
android.logcat_filters = *:S python:D

# --- 以下はデフォルト ---
[buildozer]

log_level = 2
warn_on_root = 1
