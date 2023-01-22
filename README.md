# AES File Encryption/Decryption Tool
A simple command line tool that encrypts and decrypts files using AES encryption and stores the key in a separate file.

## Installation

In order to run the script successfully, **pycryptodome** library need to be installed.

* You can install it using pip by running the following command in your terminal or command prompt:
    ```md
    pip3 install pycryptodome
    ```

* If you are using python3 or newer version, use this instead:
    ```md
    pip install pycryptodome
    ```

## Usage

The tool can be used to encrypt and decrypt files. By default, it will encrypt a file, but you can use the -d or --decrypt option to decrypt a file.

To encrypt a file:
```md
python aes_file_encryption.py <file_path> <key_path>
```

To decyrpt a file:
```md
python aes_file_encryption.py -d <file_path> <key_path>
```

The file_path argument is the path to the file you want to encrypt/decrypt. The key_path argument is the path to the file where the key will be stored/read from.

The tool will encrypt the file and store the encrypted version with the ".aes" extension. The original file will be deleted.

When decrypting a file, the decrypted version of the file will be stored in the same directory as the original file, but without the ".aes" extension.

## Example

```md
python aes_file_encryption.py documents/sample.txt keys sample.key
```
This command will encrypt the file "sample.txt" located in the "documents" directory and store the key in a file called "sample.key" located in the "keys" directory.

```md
python aes_file_encryption.py -d documents/sample.txt.aes keys/sample.key
```

This command will decrypt the file "sample.txt.aes" located in the "documents" directory using the key stored in "sample.key" located in the "keys" directory.

## Support
If you have any issues or questions, please feel free to contact me at ibrahimtahaistikbal@gmail.com

## Disclaimer

This tool is intended for legitimate and legal use only. Any unauthorized use of this tool is strictly prohibited.

## References

This tool is based on pycrypto library, you can find more information about it in their website https://www.dlitz.net/software/pycrypto/

