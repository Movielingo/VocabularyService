# Vocabulary Service

### 📖 About

VocabularyService is a comprehensive tool designed to extract, classify, and store vocabulary from subtitle files.
With the help of Spacy.io, it tags words based on their parts of speech, classifies them into CEFR levels (B2, C1,
etc.), and leverages the DeepL API for context translations. The processed data is then stored in a firestore database
for further use.

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

### ️🖥 Usage

1. **Extract Words from Subtitle Files and store movie and vocabularies in firestore**

   => adjust all constants (movie title, movie description, ...) before running)
   ```bash
   python main.py
   ```

### ⚙️ How It Works

- Reading subtitle files sentence by sentence.
- Extracting unique, meaningful words while excluding names and special terms.
- Deriving the lemma, word type, and CEFR level for each word.
- Creating or updating the vocabulary dictionary with each new word, its context sentence, translation, and timestamp.
- Storing the movie document and all vocabulary in Firestore, utilizing batch writes for efficiency.

### 🔧 Configuration

- Make sure to provide your DeepL API key in the appropriate `.env` file in the `/conf` folder for translation
  services.
- Make sure to provide a db_serviceAccount.json configuration file in the `/conf` folder be able to connect to
  your firestore db.
