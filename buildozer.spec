[app]
title = Nip
package.name = nip
package.domain = org.chikuboya
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttc
version = 0.1
requirements = python3,kivy==2.3.0,pillow,android,pyjnius,kivmob

orientation = portrait
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# 安定性を考え、APIレベルを31（Android 12相当）に設定
android.api = 31
android.minapi = 21
android.ndk = 25b
android.enable_androidx = True

# 広告ライブラリ（安定版の22.0.0）
android.gradle_dependencies = com.google.android.gms:play-services-ads:22.0.0

# ★重要：meta_dataは必ず1行ずつ別々に書く
android.meta_data = com.google.android.gms.ads.APPLICATION_ID=ca-app-pub-3940256099942544~3347511713
android.meta_data = com.google.android.gms.ads.AD_MANAGER_APP=true

[buildozer]
log_level = 2
