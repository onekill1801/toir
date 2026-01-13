from riotwatcher import TftWatcher, ApiError

API_KEY = "RGAPI-09bdb178-bcaf-455b-ac3b-e98f96492f59"
watcher = TftWatcher(API_KEY)
puuid = "eC_Ci0UV_ZSwXxElfK0XkFRzji1KwpXVeywwxD-egEelRpKr5dc2DIFBNUnrnD4AoW6uy_T15y9GmQ"
region = "sea" # VN hiện tại dùng sea hoặc asia tùy trận, nhưng VN2_... thường là cụm sea/asia

try:
    match_ids = watcher.match.by_puuid(region=region, puuid=puuid, count=1)
    print("match_detail " * 20)
    print(match_ids)
    
    if match_ids:
        match_detail = watcher.match.by_id(region=region, match_id=match_ids[0])
        # print(match_detail)
        participants = match_detail["info"]["participants"]
        # Lặp qua toàn bộ 8 người trong trận
        for player in match_detail["info"]["participants"]:
            # Lấy tên (Nếu bạn có dùng thêm logic để map PUUID sang Name)
            p_puuid = player['puuid']
            placement = player['placement']
            level = player['level']

            print(f"Match ID: {p_puuid}")
            print("-" * 30)
            print(f"My data: {player}")
            
            # Lấy danh sách các tướng (units) của họ lúc kết thúc
            units = [u['character_id'].replace('TFT13_', '') for u in player['units']]
            
            print(f"Hạng {placement}: {p_puuid[:10]}... - Level {level}")
            print(f"Đội hình cuối: {', '.join(units)}")
            print("-" * 20)

        # my_data = next(p for p in participants if p["puuid"] == puuid)

        # print(f"Match ID: {match_ids[0]}")
        # print("-" * 30)
        # print(f"My data: {my_data}")
        # print("-" * 30)
        # print(f"Hạng (Placement): {my_data['placement']}")
        # print(f"Cấp độ: {my_data['level']}")
        
        # # Sửa lỗi KeyError tại đây:
        # if 'total_damage_to_players' in my_data:
        #     print(f"Sát thương lên người chơi: {my_data['total_damage_to_players']}")
        
        # # In thêm các thông tin thú vị khác nếu muốn:
        # print(f"Vàng còn lại: {my_data.get('gold_left', 0)}")
        # print(f"Thời gian sống: {int(my_data.get('time_eliminated', 0) / 60)} phút")

except Exception as e:
    print(f"Gặp lỗi: {e}")