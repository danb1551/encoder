def decode_emojipuke(emojipuke_code):
    emojipuke_parts = emojipuke_code.split()
    text = ''

    if len(emojipuke_parts) < 3:
        raise ValueError('Invalid EmojiPuke code')

    if len(emojipuke_parts[0]) != 1 or len(emojipuke_parts[-1]) != 1:
        raise ValueError('Invalid EmojiPuke code: Missing header/footer')

    for i in range(2, len(emojipuke_parts) - 2, 3):
        if len(emojipuke_parts[i]) != 6:
            raise ValueError('Invalid EmojiPuke code: Missing print command')
        if len(emojipuke_parts[i+1]) != 1:
            raise ValueError('Invalid EmojiPuke code: Missing reset command')
        char_value = len(emojipuke_parts[i-1])
        text += chr(char_value)

    return text

if __name__ == "__main__":
    emojipuke_code = input("Zadejte EmojiPuke kód k dekódování: ")
    try:
        decoded_text = decode_emojipuke(emojipuke_code)
        print("Dekódovaný text:")
        print(decoded_text)
    except ValueError as e:
        print(f"Error: {e}")
