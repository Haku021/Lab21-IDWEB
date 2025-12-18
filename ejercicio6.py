import json

equipos=[
    {"nombre":"Real Madrid","pais":"España","nivelAtaque":95,"nivelDefensa":88},
    {"nombre":"Manchester City","pais":"Inglaterra","nivelAtaque":93,"nivelDefensa":90},
    {"nombre":"Bayern Munich","pais":"Alemania","nivelAtaque":91,"nivelDefensa":87},
    {"nombre":"PSG","pais":"Francia","nivelAtaque":94,"nivelDefensa":85},
    {"nombre":"Barcelona","pais":"España","nivelAtaque":89,"nivelDefensa":83}
]

equipos_json=json.dumps(equipos,indent=4,ensure_ascii=False)

print(equipos_json)
