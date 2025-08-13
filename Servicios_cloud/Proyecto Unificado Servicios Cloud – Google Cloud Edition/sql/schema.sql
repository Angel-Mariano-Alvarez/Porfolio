USE db_puscgce;
DROP TABLE IF EXISTS texts;
CREATE TABLE texts (
  id INT AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(120), author VARCHAR(120), language VARCHAR(10),
  created_at DATETIME, updated_at DATETIME,
  body MEDIUMTEXT,
  word_count INT, char_count INT, sentence_count INT, paragraph_count INT,
  avg_word_len DECIMAL(5,2), unique_words INT, stopwords INT,
  readability_flesch DECIMAL(6,2), flesch_kincaid DECIMAL(6,2),
  coleman_liau DECIMAL(6,2), smog DECIMAL(6,2),
  has_numbers BOOLEAN, has_punctuation BOOLEAN, has_urls BOOLEAN, has_emails BOOLEAN,
  is_spanish BOOLEAN, is_english BOOLEAN, is_clean BOOLEAN,
  topic VARCHAR(60), subtopic VARCHAR(60), keywords VARCHAR(255),
  tag1 VARCHAR(60), tag2 VARCHAR(60), tag3 VARCHAR(60), tag4 VARCHAR(60), tag5 VARCHAR(60),
  reviewer VARCHAR(120), review_notes VARCHAR(255),
  status VARCHAR(20),
  reserved1 VARCHAR(60), reserved2 VARCHAR(60), reserved3 VARCHAR(60),
  reserved4 VARCHAR(60), reserved5 VARCHAR(60), reserved6 VARCHAR(60),
  reserved7 VARCHAR(60), reserved8 VARCHAR(60), reserved9 VARCHAR(60),
  reserved10 VARCHAR(60), reserved11 VARCHAR(60), reserved12 VARCHAR(60),
  INDEX idx_lang(language), INDEX idx_status(status)
);
