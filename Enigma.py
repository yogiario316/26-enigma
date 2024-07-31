############################################################################################################################
nama = ["Yogi Ario Pratama", '2313020004', "1J", "Project Enigma"]                                                       ###
for i in nama:                                                                                                           ###
    print(i)                                                                                                             ###
                                                                                                                         ###
class Rotor:                                                                                                             ###
    def __init__(self, wiring, notch):                                                                                   ###
        self.wiring = wiring                                                                                             ###
        self.notch = notch                                                                                               ###
        self.position = 0                                                                                                ###
                                                                                                                         ###
    def encode_forward(self, c):                                                                                         ###
        idx = (ord(c) - ord('A') + self.position) % 26                                                                   ###
        return chr((ord(self.wiring[idx]) - ord('A') - self.position) % 26 + ord('A'))                                   ###
                                                                                                                         ###
    def encode_backward(self, c):                                                                                        ###
        idx = (self.wiring.index(chr((ord(c) - ord('A') + self.position) % 26 + ord('A'))) - self.position) % 26         ###
        return chr(idx + ord('A'))                                                                                       ###
                                                                                                                         ###
    def rotate(self):                                                                                                    ###
        self.position = (self.position + 1) % 26                                                                         ###
        return self.position == self.notch                                                                               ###
                                                                                                                         ###
    def set_position(self, pos):                                                                                         ###
        self.position = pos % 26                                                                                         ###
                                                                                                                         ###
class Reflector:                                                                                                         ###   
    def __init__(self, wiring):                                                                                          ###
        self.wiring = wiring                                                                                             ###
                                                                                                                         ###
    def reflect(self, c):                                                                                                ###
        idx = ord(c) - ord('A')                                                                                          ###
        return self.wiring[idx]                                                                                          ###
                                                                                                                         ###
class Enigma:                                                                                                            ###
    def __init__(self, rotors, reflector):                                                                               ###
        self.rotors = rotors                                                                                             ###
        self.reflector = reflector                                                                                       ###

    def encrypt(self, text):
        encrypted_text = []
        for char in text:
            if char.isalpha():
                char = char.upper()
                for rotor in self.rotors:
                    char = rotor.encode_forward(char)
                char = self.reflector.reflect(char)
                for rotor in reversed(self.rotors):
                    char = rotor.encode_backward(char)
                for rotor in self.rotors:
                    if not rotor.rotate():
                        break
                encrypted_text.append(char)
            else:
                encrypted_text.append(char)
        return ''.join(encrypted_text)

    def decrypt(self, text):
        # For simplicity, decryption is just encryption with rotors reset
        # The actual Enigma machine did not use separate decryption logic
        for rotor in self.rotors:
            rotor.set_position(0)
        return self.encrypt(text)

# Contoh wiring dan penggunaan
rotor1 = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", 17)  # Rotor I
rotor2 = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", 5)   # Rotor II
rotor3 = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", 22)  # Rotor III
reflector = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")  # Reflector B

enigma = Enigma([rotor1, rotor2, rotor3], reflector)

# Fungsi utama untuk menerima input pengguna dan mengenkripsinya atau mendekripsinya
def main():
    while True:
        print("--------------------------------------------")
        print("Menu:")
        print("1. Enkripsi")
        print("2. Dekripsi")
        print("3. Keluar")
        choice = input("Pilih opsi (1/2/3): ")
        print("--------------------------------------------")
        if choice == '1':
            plain_text = input("Masukkan teks untuk dienkripsi: ")
            encrypted_text = enigma.encrypt(plain_text)
            print(f"Teks terenkripsi: {encrypted_text}")
            print()
        elif choice == '2':
            encrypted_text = input("Masukkan teks untuk didekripsi: ")
            decrypted_text = enigma.decrypt(encrypted_text)
            print(f"Teks terdekripsi: {decrypted_text}")
        elif choice == '3':
            print("Terimakasih telah menggunakan aplikasi ini.")
            break
        else:
            print("Opsi tidak valid, coba lagi.")

if __name__ == "__main__":
    main()
