import datetime

def calculate_age(birth_year):
    """
    Calculates the approximate age based on the birth year.
    This function demonstrates basic arithmetic and return values.
    """
    current_year = datetime.datetime.now().year
    age = current_year - birth_year
    return age

def main():
    """
    Main function to run the interactive greeting and age calculator.
    This demonstrates user input, function calls, loops, and conditionals.
    """
    print("Merhaba! Yazılım Geliştirme Yolculuğunuza Hoş Geldiniz!") # Welcome message in Turkish
    print("Welcome to your Software Development Journey!")

    user_name = ""
    while not user_name.strip(): # Loop to ensure valid input
        user_name = input("Adınız nedir? (What is your name?): ")
        if not user_name.strip():
            print("Lütfen geçerli bir isim girin. (Please enter a valid name.)")

    print(f"Merhaba, {user_name}!") # Using f-string for greeting

    birth_year = 0
    while True:
        try:
            birth_year_str = input("Doğum yılınız nedir? (What is your birth year?): ")
            birth_year = int(birth_year_str)
            # Conditional logic to validate year range
            if 1900 < birth_year <= datetime.datetime.now().year:
                break
            else:
                print("Lütfen geçerli bir doğum yılı girin (örn: 1990). (Please enter a valid birth year, e.g., 1990.)")
        except ValueError: # Error handling for non-integer input
            print("Geçersiz giriş. Lütfen bir sayı girin. (Invalid input. Please enter a number.)")

    age = calculate_age(birth_year) # Calling the function

    print(f"{user_name}, yaklaşık yaşınız {age}.") # Displaying the calculated age

    # Conditional logic based on age
    if age < 18:
        print("Genç bir geliştirici adayı! Harika bir başlangıç. (A young developer candidate! A great start.)")
    elif 18 <= age < 30:
        print("Enerjinizle harikalar yaratabilirsiniz! (You can create wonders with your energy!)")
    else:
        print("Tecrübenizle yazılım dünyasına değer katın! (Add value to the software world with your experience!)")

    print("\nYolculuğunuzda başarılar dileriz! (We wish you success on your journey!)")

if __name__ == "__main__":
    main()
