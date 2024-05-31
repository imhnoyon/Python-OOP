class Noyon:
    Name ="Mahedi Hasan Noyon"
    Ages =22
    Depart='CSE'
    def call(self):
        print("calling someone")
    def send_message(self,phone,sms):
        print(f'sending sms to:{phone} and sms :{sms}')

My_Oject = Noyon()
My_Oject.call()
My_Oject.send_message("sansung","I love u")
