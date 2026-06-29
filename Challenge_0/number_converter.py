def arabicToGeez(arabic_number):

    if arabic_number <= 0:
        return None

    digit_symbols = {0:"", 1:"፩", 2:"፪", 3:"፫", 4:"፬", 5:"፭", 6:"፮", 7:"፯", 8:"፰", 9:"፱"}
    tens_symbols = {0:"", 10:"፲", 20:"፳", 30:"፴", 40:"፵", 50:"፶", 60:"፷", 70:"፸", 80:"፹", 90:"፺"}

    def covert_numbers_under_100(n):
        return tens_symbols[(n // 10) * 10] + digit_symbols[n%10]

    geez_num = ""

    chunks = []

    while arabic_number > 0:
        chunks.append(arabic_number % 100)
        arabic_number //= 100

    for i in range(len(chunks)-1, -1, -1):
        current = chunks[i]
        if current == 0:
            continue

        chunk_str = covert_numbers_under_100(current)

        if i > 0:
            if i % 2 == 1:
                if current == 1:
                    chunk_str = "፻"
                else:
                    chunk_str += "፻"
            else:
                chunk_str += "፼"
        
        geez_num += chunk_str
    
    return geez_num