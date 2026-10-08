# 🔐 Password Generator

A command-line Python application that generates **secure, customizable random passwords**.
Built as **Task 1 (Easy)** of the **Auspify Python Developer Internship**.

---

## 📌 Features

- **Custom length** – choose how long each password should be (minimum 4 characters)
- **Customizable character types** – capital letters, small letters, numbers, special characters
- **Strong password support** – every selected character type appears at least once in each password
- **Cryptographically secure** – uses Python's `secrets` module instead of `random`
- **Multiple passwords** – generate as many passwords as you need in one go
- **Repeat without restarting** – generate more batches in the same session
- **Input validation** – invalid or empty input never crashes the program

---

## 🛠️ Technologies & Skills

| Item | Details |
|------|---------|
| Language | Python 3.6+ |
| Modules | `secrets`, `string` (standard library only) |
| Concepts | Functions, loops, input validation, string manipulation, secure randomness |

No external packages are required.

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/syedkazim8080/password-generator.git
cd password-generator
```

### 2. Run the program

```bash
python password_generator.py
```

---

## 💻 Usage Example

```text
---------- PASSWORD GENERATOR ----------
Enter your password length (minimum 4): 12

Which types of characters do you want to include?
  Include capital letters? (yes/no): yes
  Include small letters? (yes/no): yes
  Include numbers? (yes/no): yes
  Include special characters? (yes/no): yes

How many passwords do you want to generate? 3

---------- GENERATED PASSWORDS ----------
Password 1: k#8Qz!rT2mWa
Password 2: Xn4$bLp9@eYd
Password 3: 7vC&hGu1!sRj
---------------- DONE ----------------

Generate more passwords? (yes/no): no
Thank you for using Password Generator!
```

*(Passwords above are examples; yours will be different every time.)*

---

## ⚙️ How It Works

1. The user enters the desired password length.
2. The user chooses which character groups to include.
3. For each password, the program:
   - picks one character from every selected group (guaranteeing a strong mix),
   - fills the remaining length with random characters from the combined pool,
   - shuffles the result so the pattern is unpredictable.
4. The generated passwords are displayed, and the user can generate more.

---

## 📂 Project Structure

```text
password-generator/
├── password_generator.py   # Main application
└── README.md               # Project documentation
```

---

## 🔮 Future Improvements

- Copy password to clipboard
- Save generated passwords to a file
- Password strength meter
- Option to exclude look-alike characters (`O`, `0`, `l`, `1`)
- GUI version using Tkinter

---

## 👤 Author

**Syed Kaim Ali Shah**
Python Developer Intern @ Auspify
GitHub: [@syedkazim8080](https://github.com/syedkazim8080)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
