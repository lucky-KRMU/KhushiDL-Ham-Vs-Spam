# 📨 KhushiDL Ham vs Spam — SMS Message Classifier

A deep learning project that classifies SMS messages as **Ham** (legitimate) or **Spam** using a Convolutional Neural Network (CNN) built with TensorFlow/Keras.

---

## 📖 Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Model Architecture](#model-architecture)
- [Setup & Installation](#setup--installation)
- [Usage](#usage)
- [Results](#results)
- [Author](#author)

---

## Overview

This project trains a text classification model on the **SMS Spam Collection Dataset**. Raw SMS messages are preprocessed, vectorized, and fed into a CNN that learns to distinguish spam from genuine messages. Once trained, the model can be queried interactively via a CLI script.

**Key highlights:**
- End-to-end pipeline: raw data → preprocessing → training → inference
- `TextVectorization` layer baked into the model — no external tokenizer needed at inference
- Balanced dataset (equal ham/spam samples) for unbiased training
- 75/25 train-test split with a further 20% validation split from the training set

---

## Project Structure

```
Ham Vs Spam/
│
├── code/
│   ├── notebooks/
│   │   └── main.ipynb          # Full training notebook
│   ├── testing/
│   │   └── main.py             # CLI inference script
│   └── utils/
│       ├── data-extractor.py   # Parses raw SMSSpamCollection into individual .txt files
│       └── data-refiner.py     # Balances & splits data into train/test sets
│
├── data/                       # Processed data (gitignored)
│   ├── train/
│   │   ├── ham/
│   │   └── spam/
│   └── test/
│       ├── ham/
│       └── spam/
│
├── graphs/
│   ├── accuracy.png            # Training vs validation accuracy plot
│   └── loss.png                # Training vs validation loss plot
│
├── models/
│   └── model.keras             # Saved trained model
│
├── raw data/
│   └── SMSSpamCollection       # Original dataset
│
├── requirements.txt
└── README.md
```

---

## Model Architecture

```
Input (raw SMS string)
        ↓
TextVectorization   — vocab: 5,000 tokens, sequence length: 200
        ↓
Embedding           — dim: 64, mask_zero=True
        ↓
Dropout(0.4)
        ↓
Conv1D(64, kernel=5, stride=2, activation='relu')
        ↓
GlobalAveragePooling1D
        ↓
Dense(1, activation='sigmoid')   → 0 = Ham  |  1 = Spam
```

**Training config:**
| Parameter | Value |
|-----------|-------|
| Optimizer | Adam |
| Loss | Binary Cross-Entropy |
| Epochs | 15 |
| Batch Size | 32 |
| Seed | 21 |

---

## Setup & Installation

### Prerequisites

- Python 3.10+
- `pip`

### 1 — Clone the repository

```bash
git clone <your-repo-url>
cd "Ham Vs Spam"
```

### 2 — Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate        # macOS / Linux
# venv\Scripts\activate         # Windows
```

### 3 — Install dependencies

```bash
pip install -r requirements.txt
```

### 4 — Prepare the data

The raw dataset (`SMSSpamCollection`) must be present in the `raw data/` folder before running the utilities below.

**Step 4a — Extract raw data into individual files:**
```bash
cd code/utils
python3 data-extractor.py
```
> This creates `data/ham/` and `data/spam/` directories populated with individual `.txt` message files.

**Step 4b — Balance and split the data:**
```bash
python3 data-refiner.py
```
> This equalises the ham/spam counts (random undersampling), then moves files into `data/train/` and `data/test/` with a 75/25 split.

---

## Usage

### Train the model

Open and run the full notebook:

```bash
cd code/notebooks
jupyter notebook main.ipynb
```

The notebook will:
1. Load the processed dataset
2. Build the TextVectorization + CNN model
3. Train for 15 epochs
4. Plot accuracy and loss curves → saved to `graphs/`
5. Export the trained model to `models/model.keras`

---

### Run inference (CLI)

```bash
cd code/testing
python3 main.py
```

You will be prompted to enter any SMS message and the model will respond with its verdict and confidence level:

```
Enter the Message (SMS) you received: Congratulations! You've won a free iPhone. Click here to claim.

It is a Spam Message. Kindly Ignore it.
I am 97.0% sure.
```

---

## Results

| Metric | Score |
|--------|-------|
| Training Accuracy | ~99% |
| Validation Accuracy | ~98% |

Training curves are saved in the `graphs/` folder:

| Accuracy Plot | Loss Plot |
|:---:|:---:|
| `graphs/accuracy.png` | `graphs/loss.png` |

---

## Author

**L. Pawar**

---

> *Built with TensorFlow & ❤️*
