# 🎨 Color Psychology Outfit Recommender

A **Python-based console application** that recommends outfit colors and styles based on a user’s **mood, event, season, or goal**, leveraging basic concepts of **color psychology**.  

This project enhances skills in:
- Input/output handling
- Dictionaries and mappings
- Conditional logic
- Random selections
- File handling (user history)
- Console styling (optional)

---

## ✨ Features

- Ask user for input:
  - Mood (happy, calm, confident, energetic, stressed)
  - Event type (interview, date, party, casual outing)
  - Season (summer, winter, rainy)
  - Gender (male, female, neutral)

- Match input with **color psychology mappings**:
  - 🔴 Red → Confidence, passion
  - 🔵 Blue → Calmness, trust
  - 🟢 Green → Balance, freshness
  - ⚫ Black → Power, elegance
  - 🟡 Yellow → Optimism, energy
  - ⚪ White → Purity, simplicity

- Display **outfit recommendations** with:
  - Outfit suggestion (e.g., “Try wearing a red shirt with black jeans”)
  - Seasonal suggestion (e.g., “wool jackets” for winter)
  - Random style tips / fashion quotes

- Save **user history** in a JSON file
- Support for **colored console output** (via `colorama`)
- Use of **emojis** for a fun experience (via `emoji`)

---

## 🛠️ Tools & Libraries

- **Language**: Python 3.x
- **Core modules**: `random`, `time`, `json`, `os`
- **Optional libraries**:
  - [`colorama`](https://pypi.org/project/colorama/) – for colored text
  - [`emoji`](https://pypi.org/project/emoji/) – for mood & outfit emojis

Install dependencies (optional):
```bash
pip install colorama emoji# python_based_console_application
