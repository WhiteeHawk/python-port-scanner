#  Python Port Scanner

A simple multi-threaded port scanner built in Python.
This tool is designed for educational purposes to understand how network scanning works.
---
##  Features

* Scan open ports on a target
* Multi-threaded scanning (faster performance)
* Service detection (HTTP, SSH, etc.)
* Banner grabbing
* CLI support (run using terminal commands)
* Interactive mode (user input)

---

##  Usage

###  Interactive Mode

```bash
python scanner.py
```

###  CLI Mode

```bash
python scanner.py -t scanme.nmap.org -p 1-100
```

---
##  Requirements
* Python 3.x
---

##  Example Output

```text
 OPEN | 80 | HTTP | Apache
 OPEN | 22 | SSH | OpenSSH
```

---

##  Disclaimer

This tool is for educational purposes only.
Do not use it on networks or systems without permission.

---
## 👨‍💻 Author
Abdulelah Alotaibe
