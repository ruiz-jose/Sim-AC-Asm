def generate_hex_files(file_name, data_values, instruction_code_list):
    base_name = file_name.replace('.ac', '')

    # Generar el archivo .DATA.logisim.mem para Logisim
    data_file_name_logisim = f"{base_name}.DATA.logisim.mem"
    with open(data_file_name_logisim, 'w') as data_file:
        data_file.write('v2.0 raw\n')  # Agrega el encabezado necesario para Logisim
        hex_values = ' '.join(f"{value:02X}" for value in data_values)
        data_file.write(f"{hex_values}\n")

    # Generar el archivo .TEXT.logisim.mem para Logisim
    text_file_name_logisim = f"{base_name}.TEXT.logisim.mem"
    with open(text_file_name_logisim, 'w') as text_file:
        text_file.write('v2.0 raw\n')  # Agrega el encabezado necesario para Logisim
        hex_instructions = ' '.join(instruction_code_hex for _, instruction_code_hex in instruction_code_list)
        text_file.write(f"{hex_instructions}\n")

    # Generar el archivo .DATA.cverse.mem para Circuitverse
    data_file_name_cverse = f"{base_name}.DATA.cverse.mem"
    with open(data_file_name_cverse, 'w') as data_file:
        hex_values = ' '.join(f"0x{value:02X}" for value in data_values)  # Agrega el prefijo "0x"
        data_file.write(f"{hex_values}\n")

    # Generar el archivo .TEXT.cverse.mem para Circuitverse
    text_file_name_cverse = f"{base_name}.TEXT.cverse.mem"
    with open(text_file_name_cverse, 'w') as text_file:
        hex_instructions = ' '.join(f"0x{instruction_code_hex}" for _, instruction_code_hex in instruction_code_list)  # Agrega el prefijo "0x"
        text_file.write(f"{hex_instructions}\n")

    print(f"Archivos generados para Logisim: {data_file_name_logisim}, {text_file_name_logisim}")
    print(f"Archivos generados para Circuitverse: {data_file_name_cverse}, {text_file_name_cverse}")
