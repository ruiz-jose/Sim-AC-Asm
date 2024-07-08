import os
def generate_hex_files(file_name, data_values, instruction_code_list_harvard, instruction_code_list_neumann, text_instructions_harvard):
    
    base_name = os.path.basename(file_name).replace('.ac', '')
    output_dir = "bin"
    os.makedirs(output_dir, exist_ok=True)  # Crea la carpeta si no existe


# Generar el archivo .DATA.harvard.verilog para Verilog
    data_file_name_verilog = os.path.join(output_dir, f"{base_name}.DATA.harvard.verilog")
    with open(data_file_name_verilog, 'w') as data_file:
        # Copiar los valores de datos como comentarios
        for value in data_values:
            data_file.write(f"// {value:02X}\n")
        # Escribir los valores de datos en hexadecimal, uno por línea
        for value in data_values:
            data_file.write(f"{value:02X}\n")

    # Generar el archivo .TEXT.harvard.verilog para Verilog
    text_file_name_verilog = os.path.join(output_dir, f"{base_name}.TEXT.harvard.verilog")
    with open(text_file_name_verilog, 'w') as text_file:
        # Copiar las instrucciones en ensamblador como comentarios
        # Asegúrate de que assembly_instructions_harvard esté definida y contenga las instrucciones en ensamblador
        for assembly_instruction, (_, instruction_code_hex) in zip(text_instructions_harvard, instruction_code_list_harvard):
            text_file.write(f"// {assembly_instruction}\n")
        # Escribir las instrucciones en hexadecimal, una por línea
        for _, instruction_code_hex in instruction_code_list_harvard:
            text_file.write(f"{instruction_code_hex}\n")


    # Generar el archivo .neumann.logisim.mem para Logisim
    file_name_logisim = os.path.join(output_dir, f"{base_name}.neumann.logisim.mem")
    with open(file_name_logisim, 'w') as program_file:
        program_file.write('v2.0 raw\n')  # Agrega el encabezado necesario para Logisim
        # Unir instrucciones y valores de datos en una sola lista
        hex_instructions = ' '.join(instruction_code_hex for _, instruction_code_hex in instruction_code_list_neumann)
        hex_values = ' '.join(f"{value:02X}" for value in data_values)
        combined_hex = f"{hex_instructions} {hex_values}"
        # Insertar un salto de línea cada 8 bytes en la lista combinada
        combined_hex_lines = '\n'.join([' '.join(combined_hex.split()[i:i+8]) for i in range(0, len(combined_hex.split()), 8)])
        program_file.write(f"{combined_hex_lines}\n")

    
    # Generar el archivo .DATA.harvard.logisim.mem para Logisim
    data_file_name_logisim = os.path.join(output_dir, f"{base_name}.DATA.harvard.logisim.mem")
    with open(data_file_name_logisim, 'w') as data_file:
        data_file.write('v2.0 raw\n')  # Agrega el encabezado necesario para Logisim
        hex_values = ' '.join(f"{value:02X}" for value in data_values)
        data_file.write(f"{hex_values}\n")

    # Generar el archivo .TEXT.harvard.logisim.mem para Logisim
    text_file_name_logisim = os.path.join(output_dir, f"{base_name}.TEXT.harvard.logisim.mem")
    with open(text_file_name_logisim, 'w') as text_file:
        text_file.write('v2.0 raw\n')  # Agrega el encabezado necesario para Logisim
        hex_instructions = ' '.join(instruction_code_hex for _, instruction_code_hex in instruction_code_list_harvard)
        text_file.write(f"{hex_instructions}\n")

    # Generar el archivo .DATA.harvard.cverse.mem para Circuitverse
    data_file_name_cverse = os.path.join(output_dir, f"{base_name}.DATA.harvard.cverse.mem")
    with open(data_file_name_cverse, 'w') as data_file:
        hex_values = ' '.join(f"0x{value:02X}" for value in data_values)  # Agrega el prefijo "0x"
        data_file.write(f"{hex_values}\n")

    # Generar el archivo .TEXT.harvard.cverse.mem para Circuitverse
    text_file_name_cverse = os.path.join(output_dir, f"{base_name}.TEXT.harvard.cverse.mem")
    with open(text_file_name_cverse, 'w') as text_file:
        hex_instructions = ' '.join(f"0x{instruction_code_hex}" for _, instruction_code_hex in instruction_code_list_harvard)  # Agrega el prefijo "0x"
        text_file.write(f"{hex_instructions}\n")

    print(f"Archivos generados para Logisim: {data_file_name_logisim}, {text_file_name_logisim}")
    print(f"Archivos generados para Circuitverse: {data_file_name_cverse}, {text_file_name_cverse}")
