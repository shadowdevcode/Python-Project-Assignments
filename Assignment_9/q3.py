class Temperature:

    def convertFahrenheit(self):
        self.celsius = float(input("Enter temperature in celsius: "))
        converted_temp_f = (self.celsius * 1.8) + 32
        print("Temperature in Fahrenheit is : ", converted_temp_f)

    def convertCelsius(self):
        self.fahrenheit = float(input("Enter temperature in fahrenheit: "))
        converted_temp_c = ((self.fahrenheit - 32) * 5)/9
        print("Temperature in Celsius : ", converted_temp_c)

temp1 = Temperature()
temp1.convertFahrenheit()
temp2 = Temperature()
temp2.convertCelsius()