### Week 2 Test Log: Password Strength Analyzer.

| Test Case ID | Input Password               | Expected Score | Actual Score | Shannon Entropy | Real-World Status / Outcome                                               |
| :----------- | :--------------------------- | :------------- | :----------- | :-------------- | :------------------------------------------------------------------------ |
| **TC-001**   | `password123`                | 0 / 4          | **0 / 4**    | **56.9 bits**   | **PASS** — Correctly flagged by `zxcvbn` as a common dictionary word.     |
| **TC-002**   | `Qwerty!@#`                  | 1 / 4          | **1 / 4**    | **57.5 bits**   | **PASS** — Identified as a predictable keyboard sequence despite symbols. |
| **TC-003**   | `J9#xL!2@mP`                 | 3 or 4 / 4     | **4 / 4**    | **65.6 bits**   | **PASS** — Achieved score due to high randomness and character mix.       |
| **TC-004**   | `blue-elephant-running-fast` | 4 / 4          | **4 / 4**    | **152.3 bits**  | **PASS** — High entropy proves that long passphrases are highly secure.   |
| **TC-005**   | *(Blank)*                    | 0 / 4          | **0 / 4**    | **0.0 bits**    | **PASS** — Code handled empty string input safely without crashing.       |

## Key Concepts and Definitions

### 1. Shannon Entropy
Shannon Entropy measures the architectural randomness and unpredictability of a password string, expressed in bits. It quantifies how much informational "uncertainty" exists within the password. Higher entropy values indicate a higher resistance to blind, randomized brute-force cracking attempts.

### 2. Dictionary Attack Resistance
While Shannon Entropy calculates theoretical randomness, real-world attackers utilize pre-built wordlists of commonly leaked passwords. A robust analyzer must cross-reference strings against these dictionaries. This explains why an input like `password123` exhibits theoretical entropy but fails real-world deployment metrics.

### 3. Character Space (Key Space)
Key space refers to the total pool of characters available for password creation. Limiting a password to a single character set (e.g., only lowercase letters) keeps the pool small ($26$). Incorporating uppercase letters, digits, and special symbols expands the key space to $94$, exponentially increasing the number of permutations an attacker must compute.

### 4. Human Pattern Recognition (Heuristics)
Unlike computers, humans are highly predictable. We often use common keyboard sequences (`qwerty`), date structures, or standard character substitutions (e.g., replacing 's' with '$'). Utilizing heuristic analysis via the `zxcvbn` library allows the tool to look past raw mathematical length and flag these highly predictable human habits.

## Theory Behind the Tool: Password Security Analysis

### 1. The Core Problem: The Human Factor vs. Computational Power
Traditional password security relied entirely on strict, static rules (e.g., "Must contain 8 characters, 1 number, and 1 symbol"). However, standard modern computing hardware can brute-force billions of combinations per second. Because humans find truly random strings difficult to memorize, they naturally create predictable patterns that technically satisfy these rules (e.g., `P@ssword1!`) but remain incredibly easy for modern cracking rigs to compromise. 

This tool shifts the evaluation paradigm from basic complexity rules to actual algorithmic strength and predictability.

### 2. Dual-Engine Assessment Framework
To combat modern cracking methodologies, this analyzer utilizes a defensive framework that evaluates passwords across two distinct dimensions: Structural Randomness and Behavioral Heuristics.

#### A. Structural Randomness (Information Theory)
The mathematical foundation of the tool relies on **Shannon Entropy**, which measures the pure information density of the string. It assumes an attacker is guessing completely at random and calculates how many bits of uncertainty exist based on the length ($L$) and the character pool size ($R$):

$$E = L \times \log_2(R)$$

This metric proves that increasing password length yields exponential security returns compared to merely adding complex characters to a short password.

#### B. Behavioral Heuristics (Real-World Threat Modeling)
Because automated attackers rarely guess completely at random, the tool implements a heuristic engine via the `zxcvbn` library. This engine simulates modern dictionary and rule-based cracking attacks. It tokenizes the input to look for:
* Leaked credential databases and common dictionary words.
* Common spatial patterns (e.g., keyboard walks like `qwerty`).
* Sequential numbers (`12345`) and common dates (`2026`).
* Standard l33tspeak substitutions (e.g., replacing 'o' with '0').

### 3. Conclusion
By combining pure information theory (Shannon Entropy) with behavioral simulations (`zxcvbn`), the tool provides an accurate assessment of a password's real-world resilience. It effectively identifies passwords that are mathematically complex but behaviorally weak, ensuring a more resilient defense against modern credential-stuffing and brute-force attacks.
