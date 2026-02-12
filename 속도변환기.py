def km_to_meter(x): #Km/h를 m/s로 변환
    m = x * 10/36
    print(f"{x}Km/h는 {m}m/s입니다.")

def meter_to_km(y): #m/s를 Km/h로 변환
    k = y * 36/10
    print(f"{y}m/s는 {k}Km/h입니다.")


km_to_meter(120)
