# CSV to Word Document Converter

A Python application that converts CSV files containing Multiple Choice Questions (MCQs) into formatted Word documents.

## Features

- User-friendly GUI interface
- Converts CSV files to formatted Word documents
- Groups questions by subdomain
- Includes complexity levels for each question
- Formats questions with multiple choice options
- Simple and intuitive interface

## Requirements

- Python 3.x
- Required Python packages:
  - tkinter
  - pandas
  - python-docx

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/CSV-to-Docs.git
cd CSV-to-Docs
```

2. Install the required packages:
```bash
pip install pandas python-docx
```

## Usage

1. Run the application:
```bash
python main.py
```

2. In the GUI:
   - Click "Browse CSV" to select your input CSV file
   - Click "Save As" to choose where to save the Word document
   - Click "Generate Word Document" to create the document

## CSV Format

Your CSV file should have the following columns:
- Sub-domain
- Complexity
- Question
- Choice1
- Choice2
- Choice3
- Choice4

## Output Format

The generated Word document will include:
- A main heading "MCQ Question Bank"
- Questions grouped by subdomain
- Complexity level for each question
- Question text with four multiple choice options

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
