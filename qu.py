# Script untuk menghapus tanda kutip dari file .txt

def remove_quotes_from_file(input_file):
    try:
        # Baca isi file
        with open(input_file, 'r') as file:
            lines = file.readlines()

        # Hapus tanda kutip di setiap baris
        cleaned_lines = [line.replace('"', '').strip() + '\n' for line in lines]

        # Tulis kembali ke file
        with open(input_file, 'w') as file:
            file.writelines(cleaned_lines)

        print(f"Tanda kutip berhasil dihapus dari {input_file}.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")


# Jalankan fungsi
remove_quotes_from_file('ua.txt')
