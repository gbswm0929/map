import requests

url = "https://apis-navi.kakaomobility.com/v1/directions?origin=127.10764191124568,37.402464820205246,angle=270&destination=127.11056336672839,37.39419693653072&summary=false&waypoints=127.17354989857544,37.36629687436494&priority=RECOMMEND&car_fuel=GASOLINE&car_hipass=false&alternatives=false&road_details=false"
params = {"Authorization" : "KakaoAK 84354aa98b4094d7e5733e141b136452"}

respones = requests.get(url, params=params)

print(respones.json())