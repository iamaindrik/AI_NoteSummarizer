
# 🧠 AI Note Summarizer

AI Note Summarizer is a Streamlit web application that leverages state-of-the-art NLP models to **summarize lecture notes** and generate **interactive quizzes** from the summarized content. Perfect for students, educators, and lifelong learners.

---

## ✨ Features

- 📄 Upload lecture notes in **PDF** or **TXT** format
- 🧠 Summarize content using **HuggingFace Transformers (T5 model)**
- 📝 Generate **quiz questions** from the summary
- 🎯 Interactive interface using **Streamlit**
- 🔐 Lightweight and runs on free-tier cloud hosting (like Streamlit Community Cloud)

---

## 🚀 Live Demo

🟢 [Launch on Streamlit](https://ai-note-summary.streamlit.app/)  


---

## 📥 Installation

```bash
git clone https://github.com/iamaindrik/AI_NoteSummarizer.git
cd AI_NoteSummarizer
pip install -r requirements.txt
streamlit run classnote.py
```

---

## 📦 Requirements

Your `requirements.txt` should look like:

```
streamlit
transformers
torch
PyPDF2
```

Make sure to use Python 3.8–3.11 for best compatibility.

---

## 🧪 How It Works

1. **Upload Notes**: Accepts `.pdf` or `.txt` files.
2. **Extract & Summarize**: Uses `PyPDF2` to extract text and `transformers` to summarize.
3. **Generate Quiz**: Automatically creates fill-in-the-blank style questions with multiple options.

---

## 🖼️ Screenshot

![AI Note Summarizer Screenshot](https://i.ibb.co/Gvjq3MbR/Screenshot-2025-05-31-091437.png)

---

## 📌 To-Do / Future Plans

- Add support for handwritten or image-based notes (OCR)
- Enable exporting summaries and quizzes
- User authentication for saving history

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first.

---

## 📄 License

MIT License. See `LICENSE` for more details.

---

## 🙌 Credits

- Developed by [Aindrik Sarkar](https://github.com/iamaindrik)
- NLP Model powered by 🤗 HuggingFace Transformers
