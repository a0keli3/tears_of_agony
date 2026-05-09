
label chapter4_ending:

    # ===== СТРАННЫЕ КОНЦОВКИ (проверяются первыми) =====
    
    # 1. Бред Альтер эго (зарубил всех)
    if embrace_alter and apathy >= 7 and (secret_key_office or egor_trust >= 3):
        jump ending_delirium
    
    # 2. Тишина (убить себя или всех) — только если найден ключ
    if secret_key_office and apathy >= 8 and not embrace_alter:
        jump ending_silence
    
    # ===== КОНЦОВКИ С NPC (высокое доверие) =====
    
    # 3. Коля (корги-терапия)
    if kola_friendship >= 4 and apathy <= 3 and not embrace_alter:
        jump ending_kola
    
    # 4. Лёня (крыша мира)
    if lenya_trust >= 3 and apathy <= 4 and not embrace_alter:
        jump ending_lenya
    
    # 5. Егор (Гитхаб, без примирения с Варей)
    if egor_trust >= 4 and apathy <= 4 and not embrace_alter:
        jump ending_egor
    
    # 6. Варя (стихи, без примирения с Егором)
    if varya_trust >= 5 and apathy <= 3 and not embrace_alter:
        jump ending_varya
    
    # 7. Варя и Егор (история с двух сторон — НЕ примирение)
    if varya_trust >= 4 and egor_trust >= 3 and apathy <= 3 and not embrace_alter:
        jump ending_varya_egor
    
    # ===== ОСНОВНЫЕ КОНЦОВКИ (из пролога) =====
    
    # 8. Ни с кем не подружился — все считают странным
    if egor_trust <= 1 and varya_trust <= 1 and kola_friendship <= 1 and lenya_trust <= 1 and not embrace_alter:
        jump ending_stranger
    
    # 9. Принятие
    if embrace_alter and apathy <= 3:
        jump ending_acceptance
    
    # 10. Слияние
    if embrace_alter and apathy >= 6:
        jump ending_merger
    
    # 11. Одиночество
    if not embrace_alter and apathy <= 4:
        jump ending_loneliness
    
    # 12. Распад (дефолт, если ничего не подошло)
    else:
        jump ending_collapse