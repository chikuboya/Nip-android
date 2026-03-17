[app]

# (str) Title of your application
title = Nip

# (str) Package name
package.name = nip

# (str) Package domain (needed for android packaging)
package.domain = org.chikuboya

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (ttcフォントを含める設定)
source.include_exts = py,png,jpg,kv,atlas,ttc

# (list) List of inclusions using pattern matching
source.include_patterns = assets/*,images/*.png

# (str) Application version
version = 0.1

# (str) Icon of the application
icon.filename = %(source.dir)s/icon.png

# ★ 依存関係: kivmobとpyjniusを必ず含めます
requirements = python3,kivy==2.3.0,pillow,jnius,kivmob

# (str) Supported orientation
orientation = portrait

# (bool) Fullscreen mode
fullscreen = 1

# ★ 権限: 広告取得にインターネット接続が必要です
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# ★ Android SDK/NDK 設定
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21

# (bool) Use skip_update to skip sdk/ndk update
android.skip_update = False

# (bool) Use accept_sdk_license to accept sdk license
android.accept_sdk_license = True

# ★ Gradle依存関係: Google Play Services Ads を追加
android.gradle_dependencies = 'com.google.android.gms:play-services-ads:22.6.0'

# ★ メタデータ: AdMob App ID (これを忘れるとクラッシュします)
# ※以下はGoogle提供のテスト用App IDです。本番公開時は自分のIDに書き換えてください。
android.meta_data = com.google.android.gms.ads.APPLICATION_ID=ca-app-pub-3940256099942544~3347511713

# (list) Android architecture to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) enables Android auto backup
android.allow_backup = True

# (int) Log level (2 = DEBUG)
log_level = 2

# -----------------------------------------------------------------------------
# Buildozer sections
# -----------------------------------------------------------------------------

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = off, 1 = on)
warn_on_root = 1

# (str) Path to build artifacts
# build_dir = ./.buildozer

# (str) Path to bin directory
# bin_dir = ./bin
