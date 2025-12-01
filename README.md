# Hash_CrackerV1
A small Python tool that shows how hash comparison works and why strong passwords matter. Intended for learning and authorized testing only.
Hashing and Brute-Force Demonstration Script

This project is a simple Python script designed to demonstrate how hashing works and why strong, unpredictable passwords are important. It shows how a brute-force style process can generate large numbers of candidate strings and compare their hashes against a user-supplied value. This is intended for learning and security awareness only.

Purpose

The script provides a hands-on way to explore:

How hashing algorithms such as MD5, SHA-1, SHA-256, and SHA-512 operate.

How candidate inputs can be generated and hashed.

Why weak passwords are vulnerable to automated guessing attempts.

How long brute-force processes can take in practice.

It is not intended for unauthorized access or use on systems without permission.

Features

Supports hash algorithms: md5, sha1, sha256, and sha512

Reads base words from a wordlist file

Generates variations by appending numbers and symbol patterns

Allows optional printing of each generated value

Tracks attempts and total time

Uses only the Python standard library

How the Script Works

The script reads each line from a wordlist file such as rockyou.txt.

For each word, it generates variations by appending a numerical sequence and a set of predefined symbols.

Each generated value is hashed using the selected hash function.

The script checks whether the generated hash matches the target hash provided by the user.

When finished, it reports whether a match was found, how long the process took, and how many attempts were made.

This process illustrates how brute-force and wordlist-based guessing work at a fundamental level and why long, complex, and unpredictable passwords are necessary.

Requirements

Python 3.8 or newer

A wordlist text file (default name: rockyou.txt)

No external dependencies
