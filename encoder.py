def encode_text_to_emojipuke(text):
    emojipuke_code = 'y '  # začátek programu

    for char in text:
        char_value = ord(char)  # ASCII hodnota znaku
        # přičteme k hodnotě paměti
        emojipuke_code += ('y' * char_value) + ' '
        # vypíšeme hodnotu paměti jako ASCII znak
        emojipuke_code += 'y' * 6 + ' '
        # resetujeme hodnotu paměti na 0
        emojipuke_code += 'y '

    emojipuke_code += 'y'  # konec programu

    return emojipuke_code

if __name__ == "__main__":
    text_to_encode = input("Zadejte text k zakódování: ")
    emojipuke_encoded_text = encode_text_to_emojipuke(text_to_encode)
    print("Zakódovaný text v EmojiPuke:")
    print(emojipuke_encoded_text)
