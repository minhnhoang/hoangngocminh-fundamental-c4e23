port = {
    "hph": "Hai Phong",
    "sgn": "Ho Chi Minh",
    "han": "Noi Bai",
    "vut": "Vung Tau",
    "dan": "Da Nang" 
}
print(*port.keys())

while True:
    code = input("Your code: ")
    if code in port:
        print("Port name:", port[code])
    
    else:
        add = input("Code not found, do you want to contribute this port? (Y/N)").upper()
        if add == "Y":
            port[code] = input("Port name: ")
        
         