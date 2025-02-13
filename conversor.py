def base_to_decimal(value, base):
    try:
        if '.' in value:  # Verifica se há uma parte decimal
            integer_part, decimal_part = value.split('.')
            integer_value = int(integer_part, base)
            decimal_value = sum(int(digit, base) * (base ** -i) for i, digit in enumerate(decimal_part, start=1))
            return integer_value + decimal_value
        else:
            return int(value, base)
    except ValueError:
        print("Invalid input for the specified base.")
        return None

def decimal_to_base(value, base):
    try:
        integer_part = int(value)
        decimal_part = value - integer_part
        
        # Conversão da parte inteira
        if base == 2:
            result = bin(integer_part)[2:]  # Convert to binary
        elif base == 8:
            result = oct(integer_part)[2:]  # Convert to octal
        elif base == 16:
            result = hex(integer_part)[2:].upper()  # Convert to hexadecimal
        else:
            print("Invalid base.")
            return None
        
        # Conversão da parte decimal
        if decimal_part > 0:
            result += '.'
            while decimal_part > 0:
                decimal_part *= base
                digit = int(decimal_part)
                if base == 2:
                    result += str(digit)
                elif base == 8:
                    result += oct(digit)[2:]  # Octal representation
                elif base == 16:
                    result += hex(digit)[2:].upper()  # Hexadecimal representation
                decimal_part -= digit

        return result
    except ValueError:
        print("Invalid decimal number.")
        return None

def print_group_info():
    group_info = [
        {"RA": "10723789", "Name": "Joao Reiss"},
        {"RA": "10445016", "Name": "Leonardo Cruz"},
        {"RA": "10723361", "Name": "Sofia Cavalcanti"},
        {"RA": "10403255", "Name": "Joao Trindade"},
        {"RA": "10723221", "Name": "Alessandro Pimenta"},
        {"RA": "10729470", "Name": "Vinicius Pereira"},
        {"RA": "10437138", "Name": "Lucas Nigro"},
    ]
    print("Group Information:")
    for member in group_info:
        print(f"RA: {member['RA']}, Name: {member['Name']}")

def main():
    while True:
        print("\nMenu:")
        print("[1] - Convert from binary/octal/hexadecimal to decimal")
        print("[2] - Convert from decimal to binary/octal/hexadecimal")
        print("[3] - Group Information (print RA + Name of each member)")
        print("[4] - Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            value = input("Enter the value to convert: ")
            base = int(input("Enter the base (2 for binary, 8 for octal, 16 for hexadecimal): "))
            result = base_to_decimal(value, base)
            if result is not None:
                print(f"The decimal value is: {result}")

        elif choice == '2':
            value = float(input("Enter the decimal value to convert: "))
            base = int(input("Enter the base to convert to (2 for binary, 8 for octal, 16 for hexadecimal): "))
            result = decimal_to_base(value, base)
            if result is not None:
                print(f"The value in base {base} is: {result}")

        elif choice == '3':
            print_group_info()

        elif choice == '4':
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()