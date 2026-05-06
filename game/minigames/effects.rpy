# -------------визуальные эффекты для игр
image flash_green:
    Solid("#44ff44", xysize=(1920, 1080))
    alpha 0.0
    linear 0.05 alpha 0.3
    linear 0.3 alpha 0.0

image flash_red:
    Solid("#ff4444", xysize=(1920, 1080))
    alpha 0.0
    linear 0.05 alpha 0.3
    linear 0.3 alpha 0.0

image flash_gray:
    Solid("#666666", xysize=(1920, 1080))
    alpha 0.0
    linear 0.05 alpha 0.2
    linear 0.3 alpha 0.0

image effect_correct:
    Solid("#88ff88", xysize=(400, 400))
    alpha 0.0
    linear 0.05 alpha 0.7
    linear 0.2 alpha 0.0

image effect_wrong:
    Solid("#ff4444", xysize=(400, 400))
    alpha 0.0
    linear 0.05 alpha 0.7
    linear 0.2 alpha 0.0