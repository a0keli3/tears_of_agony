
label chapter4_ending:
 
    # 1. Бред Альтер эго (зарубил всех)
    if embrace_alter and apathy >= 7 and (secret_key_office or sergy_trust >= 3):
        jump ending_delirium
    
    # 2. Тишина (убить себя или всех) — только если найден ключ
    if secret_key_office and apathy >= 8 and not embrace_alter:
        jump ending_silence
    
    # ===== КОНЦОВКИ С NPC (высокое доверие) =====
    
    # 3. Коля
    if kola_friendship >= 4 and apathy <= 3 and not embrace_alter:
        jump ending_kola
    
    # 4. Лёня
    if lenya_trust >= 3 and apathy <= 4 and not embrace_alter:
        jump ending_lenya
    
    # 5. Сергей
    if sergy_trust >= 4 and apathy <= 4 and not embrace_alter:
        jump ending_sergy
    
    # 6. Алиса
    if alice_trust >= 5 and apathy <= 3 and not embrace_alter:
        jump ending_alice
    
    # 7. Алиса и Сергей
    if alice_trust >= 4 and sergy_trust >= 3 and apathy <= 3 and not embrace_alter:
        jump ending_alice_sergy
    
    # ===== ОСНОВНЫЕ КОНЦОВКИ (из пролога) =====
    
    # 8. Ни с кем не подружился — все считают странным
    if sergy_trust <= 1 and alice_trust <= 1 and kola_friendship <= 1 and lenya_trust <= 1 and not embrace_alter:
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