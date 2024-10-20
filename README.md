# **Diffie-Hellman Key Exchange Simulation**

This project demonstrates a simplified version of the **Diffie-Hellman key exchange** using Python's `Crypto.Util.number` module. The code generates large prime numbers to simulate the process of two parties securely sharing a secret key over an insecure channel.

---

## **Table of Contents**
1. [Overview](#overview)  
2. [How it Works](#how-it-works)  
3. [Installation](#installation)  
4. [Usage](#usage)  
5. [Example Output](#example-output)  
6. [Technologies Used](#technologies-used)  
7. [License](#license)  

---

## **Overview**

The code generates two large prime numbers and performs modular exponentiation to simulate the Diffie-Hellman key exchange protocol. The goal is to show how two parties can independently compute the same secret key, ensuring that communication remains secure.

---

## **How it Works**

1. **Generate Prime Numbers:**  
   - Two large primes, `a` and `b`, are generated with a bit length of 2048.  
   - A 1024-bit prime `p` is also generated, serving as the modulus for the key exchange.  

2. **Base Generator:**  
   - The value of `g` (generator) is set to 65537, a common choice in cryptographic algorithms.

3. **Public Key Computation:**  
   - Both parties compute their public keys `A` and `B` using modular exponentiation:  
     - \( A = (g^a) \bmod p \)  
     - \( B = (g^b) \bmod p \)

4. **Shared Secret Computation:**  
   - Each party computes the shared secret using the other’s public key:  
     - \( S1 = (B^a) \bmod p \)  
     - \( S2 = (A^b) \bmod p \)

5. **Verification:**  
   - If `S1` equals `S2`, the key exchange was successful, and both parties have the same shared secret.

---

## **Installation**

Ensure you have Python installed. Then, install the **PyCryptodome** library, which provides the `Crypto.Util.number` module.

```bash
pip install pycryptodome
```

---

## **Usage**

1. Clone this repository or copy the code into a local file (e.g., `diffie_hellman.py`).  
2. Run the script using the following command:

```bash
python diffie_hellman.py
```

---

## **Example Output**

```
True
```

This output confirms that both parties independently computed the same shared secret.

---

## **Technologies Used**

- **Python**  
- **PyCryptodome Library** (`Crypto.Util.number`)

---

## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

This README ensures clarity and professionalism, providing all necessary information for users to understand, install, and run your code.
