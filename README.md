# Python Binary Search

## 📘 Overview

This repository contains a Python implementation of the **Binary Search** algorithm.

The program searches for a given key in a sorted array and returns the index of the key if it is found. If the key is not present, it returns `-1`.

---

## 📌 How It Works

Binary Search works by repeatedly dividing the search range into two halves.

The algorithm compares the key with the middle element:

- If the middle element is equal to the key, the index is returned.
- If the key is greater than the middle element, the search continues in the right half.
- If the key is smaller than the middle element, the search continues in the left half.
- If the search range becomes empty, `-1` is returned.

---

## 💡 Example

Given:

```text
[10, 20, 30, 40, 50, 60, 70, 80]
