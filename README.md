# Password Generator Module

This module provides a set of classes for generating passwords with various criteria. The goal is to offer flexibility and customization in creating passwords based on different requirements.

## Classes:

### 1. PasswordGenerator (ABC)
- Abstract base class for password generators.

### 2. PinPassword
- Generates a numeric PIN password.

#### Parameters:
- `length` (int, optional): Length of the PIN password (default is 8).

### 3. RandomPassword
- Generates a random alphanumeric password with optional inclusion of numbers and symbols.

#### Parameters:
- `length` (int, optional): Length of the password (default is 8).
- `include_numbers` (bool, optional): Include numbers in the password (default is False).
- `include_symbols` (bool, optional): Include symbols in the password (default is False).

### 4. MemorablePassword
- Generates a memorable password using words from a vocabulary.

#### Parameters:
- `num_of_words` (int, optional): Number of words in the password (default is 4).
- `separator` (str, optional): Separator between words in the password (default is '_').
- `capitalization` (bool, optional): Capitalize the words in the password (default is False).
- `vocabs` (list, optional): List of words to choose from (default is NLTK English words).

## Usage:
Instantiate an object of the desired password generator class and call the `generate()` method to get a password.

### Example:
```python
from password_generator import MemorablePassword

p_obj = MemorablePassword(num_of_words=5, separator='**', capitalization=True)
generated_password = p_obj.generate()
print(generated_password)
