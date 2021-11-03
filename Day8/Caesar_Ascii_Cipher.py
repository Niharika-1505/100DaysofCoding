def caesar(message, shift_value, shift_direction):
    final_message = ""
    if shift_direction.lower() == "decode":
        shift_value *= -1
    for i in list(message):
        ascii_value = ord(i) + shift_value
        final_message += str(chr(ascii_value))
    print(f"{shift_direction}d message is: {final_message} ")


should_end = False
while not should_end:
    encode_or_decode = str(input("Do you want to Encode or Decode: "))
    if encode_or_decode.lower() == "encode" or encode_or_decode.lower() == "decode":
        actual_Message = str(input("The message to be encrypted: "))
        value = int(input("Type the encrypting shift value:"))
        caesar(message=actual_Message, shift_value=value, shift_direction=encode_or_decode)
    else:
        print("Please enter the spelling correctly")
        break
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart.lower() == "no":
        should_end = True
        print("Goodbye")
