# Vidio_Agent
Transform videos into actionable insights with AI-powered transcription, summarization, key decision extraction, and RAG-based question answering
# 🎥 AI Video Assistant

An AI-powered Video & Meeting Assistant that can:

✅ Extract audio from YouTube videos or local files  
✅ Transcribe speech using Whisper AI or Sarvam AI  
✅ Generate smart summaries  
✅ Extract Action Items, Key Decisions, and Open Questions  
✅ Build a RAG (Retrieval-Augmented Generation) knowledge base  
✅ Chat with video content using Mistral AI  
✅ Beautiful Streamlit Web Interface

---

## 🚀 Features

### 📥 Video Processing

- YouTube URL support
- Local audio/video file support
- Automatic audio extraction
- Audio chunking for long videos    

### 🎙️ Speech-to-Text

Supports:

- OpenAI Whisper (English)
- Sarvam AI (Hinglish)

### 📝 AI Summarization

Generate:

- Video Title
- Summary
- Action Items
- Key Decisions
- Open Questions

### 🤖 Chat With Video

Ask questions like:

- What is this video about?
- Summarize the key points.
- What tools were discussed?
- What decisions were made?
- Explain the project architecture.

Powered by:

- ChromaDB
- LangChain
- Mistral AI
- Sentence Transformers

---

## 🏗️ Project Architecture

```text
YouTube URL / Local File
            │
            ▼
     Audio Extraction
            │
            ▼
      Audio Chunking
            │
            ▼
      Transcription
   (Whisper / Sarvam)
            │
            ▼
      Full Transcript
            │
    ┌───────┼────────┐
    ▼       ▼        ▼
 Summary  Decisions Actions
            │
            ▼
      Vector Database
         (Chroma)
            │
            ▼
        RAG Engine
            │
            ▼
      Chat Interface
```

---

## 📂 Project Structure

```text
AI_Video_Assistant/
│
├── app.py
├── main.py
├── requirements.txt
├── .env
│
├── core/
│   ├── transcriber.py
│   ├── summarizer.py
│   ├── extractor.py
│   ├── vector_store.py
│   └── rag_engine.py
│
├── utils/
│   └── audio_processor.py
│
├── downloads/
│
└── vector_db/
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/AI-Video-Assistant.git

cd AI-Video-Assistant
```

### Create Virtual Environment

```bash
python -m venv .venv
```

Activate:

Windows

```bash
.venv\Scripts\activate
```

Linux / Mac

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
MISTRAL_API_KEY=your_mistral_api_key

SARVAM_API_KEY=your_sarvam_api_key

WHISPER_MODEL=small

SARVAM_STT_MODEL=saaras:v2.5
```

---

## ▶️ Running the Application

### Streamlit UI

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

## 💬 Example Questions

After processing a video:

```text
What is this video about?

Summarize the key points.

What technologies were discussed?

What action items were mentioned?

Explain the architecture discussed in the video.

What decisions were made?

Give me all important insights.
```

---

## 🛠️ Tech Stack

### AI / LLM

- Mistral AI
- Whisper
- Sarvam AI

### Frameworks

- LangChain
- Streamlit

### Vector Database

- ChromaDB

### Embeddings

- Sentence Transformers
- all-MiniLM-L6-v2

### Audio Processing

- FFmpeg
- Pydub
- yt-dlp

---

## 📸 Screenshots

### Home Screen
<img width="1902" height="867" alt="Screenshot 2026-06-16 222433" src="https://github.com/user-attachments/assets/8691b734-c63c-4690-92ef-934dee42f19c" />

```

### Results Screen

<img width="1427" height="765" alt="Screenshot 2026-06-16 222527" src="https://github.com/user-attachments/assets/ea9fa168-dc4d-42a8-80ae-8e286a5151a8" />

```

### Chat Interface

```
<img width="1408" height="667" alt="Screenshot 2026-06-16 222636" src="https://github.com/user-attachments/assets/b4749ee5-cace-4e90-8b24-9b691b3d5582" />

---

## 🔮 Future Improvements

- Speaker Diarization
- Multi-language Support
- PDF Export
- Meeting Minutes Generator
- Video Timestamp Referencing
- Live Meeting Assistant
- Cloud Deployment
- User Authentication

---

## 🤝 Contributing

Contributions are welcome.

Fork the repository and submit a Pull Request.

---

## 📜 License

MIT License

---

## 👨‍💻 Author

Twinkle Patel

GitHub: https://github.com/yourusername

LinkedIn: https://linkedin.com/in/yourprofile
