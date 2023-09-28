# VocabularyService

### 📖 About

VocabularyService is a comprehensive tool designed to extract, classify, and store vocabulary from subtitle files. With the help of Spacy.io, it tags words based on their parts of speech, classifies them into CEFR levels (B2, C1, etc.), and leverages the DeepL API for context translations. The processed data is then stored in a database for further use.

### 🚀 Features

- **Subtitle Word Extraction**: Extracts words seamlessly from subtitle files.
- **Part-of-Speech Tagging with Spacy.io**: Classifies words into nouns, verbs, adjectives, etc.
- **CEFR Level Classification**: Classifies words into CEFR levels like B2, C1, etc.
- **Context Translations with DeepL API**: Provides context translations of words and phrases for better understanding.
- **Database Integration**: Stores processed data efficiently in a database.

### 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/VocabularyService.git
   ```
   
2. Navigate to the project directory:
   ```bash
   cd VocabularyService
   ```

3. Install dependencies using Poetry:
   ```bash
   poetry install
   python -m spacy download en_core_web_sm
   ```

### 🖥️ Usage

1. **Extract Words from Subtitle Files**:
   ```bash
   python subtitle_words.py [PATH_TO_SUBTITLE_FILE]
   ```

2. **Tag Words with Spacy.io**:
   ```bash
   python word_tagging.py
   ```

3. **Classify Words into CEFR Levels**:
   ```bash
   python word_level.py
   ```

4. **Translate Words with DeepL**:
   ```bash
   python translation.py
   ```

### 🔧 Configuration
  
- Make sure to provide your DeepL API key in the appropriate configuration file for translation services.
