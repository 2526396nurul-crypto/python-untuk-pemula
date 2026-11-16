# Python untuk Pemula

Repositori tugas Python untuk Pemula (Santrikoding), dikerjakan oleh Nurul Azizah, SMKN 2 Subang.

## Daftar bab

1. Pengenalan dan Instalasi: `hello.py`
2. Variabel dan Tipe Data: `variable_numbers.py`, `variable_string.py`, `variable_boolean.py`
3. Operator: `operator_aritmatika.py`, `operator_comparison.py`, `operator_logical.py`
4. Kondisi If Else: `condition_if.py`, `condition_if_elif.py`, `condition_if_else.py`
5. Perulangan: `loop_for_1.py`, `loop_for_2.py`, `loop_while.py`, `loop_for_break.py`
6. Lists dan Dictionaries: `lists_create.py`, `lists_add_item.py`, `lists_delete_item.py`, `dictionaries_create.py`, `dictionaries_add_item.py`, `dictionaries_update_item.py`, `dictionaries_delete_item.py`
7. Function: `function_create.py`, `function_arguments_1.py`, `function_arguments_2.py`, `function_arbitrary_arguments.py`, `function_arbitrary_keyword_arguments.py`, `function_default_value_arguments.py`
8. Class dan Object: `class_create.py`, `class_create_method.py`, `class_self_parameter.py`
9. PIP dan Virtual Environments: `pip_flask_versi.py`
10. Konfigurasi IDE: `KONFIGURASI_IDE.md` dan `.gitignore`
11. README dan requirements: `README.md` dan `requirements.txt`

## Catatan pengerjaan

- Nama berkas mengikuti pola penamaan modul Santrikoding. Berkas yang tidak ada di modul dibuat sendiri: `pip_flask_versi.py` (bab 9) dan `KONFIGURASI_IDE.md` (bab 10).
- Struktur dan konsep tiap berkas mengikuti contoh di modul, sedangkan isi datanya berasal dari pengerjaan sendiri.
- Di Arch Linux, `pip install` di luar Virtual Environment ditolak (PEP 668), jadi semua pemasangan paket dilakukan di dalam `.venv`.

## Cara menjalankan

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python hello.py
```

## Bukti hasil

Screenshot hasil tiap bab ada di folder `screenshots/`.
