import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
def maker():
    qr.add_data(choose)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"{filename}.png")

urllist = ["1","URL","url"]
textlist = ["2","TEXT","text"]
phonelist = ["3","PHONE","phone"]
wifilist = ["4","WIFI","wifi"]

print("""
1) URL       3) PHONE
2) TEXT      4) WIFI
""")
option = str(input("Select One: "))

if option in urllist:
    choose = str(input("Write the URL:"))
    filename = str(input("Name of the File to be Created(without extension): ")) 
    maker()


elif option in textlist:
    choose = str(input("Write the TEXT:"))
    filename = str(input("Name of the File to be Created(without extension): ")) 
    maker()


elif option in phonelist:
    choose = str(input("Write the PHONE:"))
    filename = str(input("Name of the File to be Created(without extension): ")) 
    maker()


elif option in wifilist:
    ssid = str(input("Write the SSID(Wifi Name): "))
    password = str(input("Write the Password: "))
    encryption = str(input("Write Type of Encryption: "))
    filename = str(input("Name of the File to be Created(without extension): ")) 
    choose = f"WIFI:T:{encryption};S:{ssid};P:{password};;"
    maker()

else:
    print("Not Found.")



