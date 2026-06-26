# Final Project Report
**Project 1: Advanced Desktop Password Strength Analyzer**

## 1. Executive Summary
The objective of this project was to design and develop an application capable of auditing password strength. Traditional security rules requiring arbitrary character types often result in predictable human patterns (e.g., 'P@ssword1') that fail to resist modern automated cracking methodologies.

This application provides real-time mathematical and behavioral feedback to users, ensuring they can craft passwords resilient against both brute-force and dictionary-based attacks.

## 2. Architectural Design & Security Theory

The tool processes user inputs simultaneously across two distinct analytical engines before rendering a verdict in the application window.

 **A. Structural Randomness (Shannon Entropy)**
 
  The mathematical foundation relies on Information Theory via the **Shannon Entropy** calculation. This metric assumes an attacker is guessing characters completely at random and determines the total bits of "uncertainty" within the string. The algorithm maps user input to a dynamic character key space ($R$) based on detected character variety (lowercase = 26, uppercase = 26, digits = 10, symbols = 32) and applies the formula against length ($L$): $$E = L \times \log_2(R)$$ This calculation demonstrates that exponential security returns are gained by expanding structural length rather than merely relying on basic symbol substitutions. 
  
  **B. Behavioral Heuristics (Real-World Threat Modeling)**
  
  Because modern threats leverage pre-compiled leaked databases rather than blind guessing, the application implements a heuristic evaluation engine powered by the `zxcvbn` library. Developed by Dropbox, this engine tokenizes inputs to evaluate resistance against realistic cracking techniques, explicitly tracking: 
  * High-frequency dictionary matches and standard leaked passwords. 
  * Spatial keyboard sequences (e.g., "qwerty", "asdf"). 
  * Human-predictable substitutions (l33tspeak, capitalization anchors). 
  * Sequential patterns, repeated strings, and common dates.

## 3. Empirical Test Log & Functional Validation

| Test Case ID | Input Password               | Expected Score | Actual Score | Shannon Entropy | Real-World Status / Outcome                                               |
| :----------- | :--------------------------- | :------------- | :----------- | :-------------- | :------------------------------------------------------------------------ |
| **TC-001**   | `password123`                | 0 / 4          | **0 / 4**    | **56.9 bits**   | **PASS** — Correctly flagged by `zxcvbn` as a common dictionary word.     |
| **TC-002**   | `Qwerty!@#`                  | 1 / 4          | **1 / 4**    | **57.5 bits**   | **PASS** — Identified as a predictable keyboard sequence despite symbols. |
| **TC-003**   | `J9#xL!2@mP`                 | 3 or 4 / 4     | **4 / 4**    | **65.6 bits**   | **PASS** — Achieved score due to high randomness and character mix.       |
| **TC-004**   | `blue-elephant-running-fast` | 4 / 4          | **4 / 4**    | **152.3 bits**  | **PASS** — High entropy proves that long passphrases are highly secure.   |
| **TC-005**   | *(Blank)*                    | 0 / 4          | **0 / 4**    | **0.0 bits**    | **PASS** — Code handled empty string input safely without crashing.       |

## 4. Architectural Core Concepts & Definitions

* **Shannon Entropy (Bits):** A representation of binary bits required to break a random string. Every additional bit doubles the complexity for a blind brute-force rig. Scores $>60$ bits represent a strong baseline defense. 
* **Dictionary Attack:** An optimized hacking technique using wordlists of known terms and past data leaks. This explains why `password123` fails real-world metrics despite its 56.9-bit raw math profile.
* **Key Space Size:** The cumulative pool of possible values available per character index. Scaling the key space from $26$ (lowercase) to $94$ (alphanumeric + symbols) increases total computational requirements exponentially for attackers. 
* **Heuristics:** Rules-of-thumb and pattern matching that look beyond hard math to account for highly predictable, flawed human behavioral choices.

