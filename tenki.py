import scratchattach as scratch3,time,random,requests
session = scratch3.login("kannbo", ) # 自分のパスワード
conn = session.connect_cloud("961033085") # project_id
print(1)
# https://scratch.mit.edu/projects/767766792/
variables = scratch3.get_cloud("961033085") # Returns a dict with all cloud var values
print(1)
print(variables)
print(variables.keys())
while True:
    for name in variables.keys():
        #print(variables)
        value = variables[name]
        req=requests.get("https://api.open-meteo.com/v1/forecast?latitude=35.41&longitude=139.41&current=temperature_2m,relative_humidity_2m,precipitation,weather_code&daily=precipitation_sum&timezone=Asia%2FTokyo",
                          headers={"content-type": "application/json"}).json()
        #print(req)
        kion=req["current"]["temperature_2m"]
        situdo=req["current"]["relative_humidity_2m"]
        tenki=req["current"]["weather_code"]
        #print(1)
        conn.set_var("気温",kion)
        conn.set_var("湿度",situdo)
        conn.set_var("天気",tenki)
        time.sleep(30)
conn.disconnect()
