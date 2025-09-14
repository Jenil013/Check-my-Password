# Password Pwned Checker

This Python project checks if your passwords have been compromised in known data breaches using the [Have I Been Pwned](https://haveibeenpwned.com/API/v3#PwnedPasswords) API.

## Features

- Reads a list of passwords from a file
- Checks each password securely (using k-Anonymity, no full password sent)
- Reports if a password has been leaked and how many times

## Usage

1. **Add your passwords**  
   Edit the [`passwords.txt`](passwords.txt) file and add each password you want to check on a new line (skip the first line, which is a comment).

2. **Install dependencies**  
   Make sure you have Python 3 and `requests` installed:
   ```sh
   pip install requests
   ```

3. **Run the checker**  
   ```sh
   python checkmypassword.py
   ```

4. **View results**  
   The script will print whether each password has been leaked and how many times.

## File Structure

- [`checkmypassword.py`](checkmypassword.py): Main script to check passwords.
- [`passwords.txt`](passwords.txt): List of passwords to check.

## Example Output

```
The given password Jenil123 has been leaked 2 times. You should probably change it.
The given password Patel234 is safe, secure and never been leaked.
The given password Helllo483949 is safe, secure and never been leaked.
```

## Disclaimer

- Do **not** share your passwords or this file with anyone.
- For best security, use a password manager and generate strong, unique passwords.

## License

This project is for educational purposes.