[app]
title = Nip
package.name = nip
package.domain = org.chikuboya
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttc
version = 0.1
icon.filename = %(source.dir)s/icon.png

# 必須ライブラリ
requirements = python3,kivy==2.3.0,pillow,android,pyjnius,kivmob

orientation = portrait
fullscreen = 1

# 広告通信に必要な権限
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# Android SDK/NDK 設定（安定性を考慮しAPI 31）
android.api = 31
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21

# Gradle 依存関係
android.gradle_dependencies = com.google.android.gms:play-services-ads:22.0.0

# AndroidX 有効化
android.enable_androidx = True

# ★重要：meta_dataは必ず「1つの項目名」に「カンマ区切り」で書く
android.meta_data = com.google.android.gms.ads.APPLICATION_ID=ca-app-pub-3940256099942544~3347511713, com.google.android.gms.ads.AD_MANAGER_APP=true

log_level = 2

[buildozer]
log_level = 2
warn_on_root = 1
