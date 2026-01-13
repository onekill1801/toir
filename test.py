from riotwatcher import RiotWatcher, ApiError

API_KEY = "RGAPI-09bdb178-bcaf-455b-ac3b-e98f96492f59"

watcher = RiotWatcher(API_KEY)

try:
    # Thay gameName + tagLine cho đúng
    account = watcher.account.by_riot_id(
        region="asia",
        game_name="Level 1",
        tag_line="CNN"
    )

    print("✅ API KEY HỢP LỆ")
    print("PUUID:", account["puuid"])

except ApiError as err:
    if err.response.status_code == 401:
        print("❌ API KEY KHÔNG HỢP LỆ hoặc HẾT HẠN")
    elif err.response.status_code == 403:
        print("❌ API KEY BỊ TỪ CHỐI")
    elif err.response.status_code == 404:
        print("⚠️ KHÔNG TÌM THẤY RIOT ID (nhưng API KEY vẫn OK)")
    elif err.response.status_code == 429:
        print("⚠️ BỊ RATE LIMIT")
    else:
        print("❌ LỖI KHÁC:", err)
