
# Tamul AI

Tamul AI is an AI-powered podcast agent featuring dual hosts for interactive discussions and real-time user Q&A. It leverages GenAI, Google TTS/STT, multithreading, and Redis caching for seamless, near-zero latency experiences.

## 🚀 Features

- 🎙️ Dual AI hosts for dynamic conversations  
- ⚡ Real-time user Q&A integration  
- 🧵 4-queue multithreading architecture for high performance  
- 🗃️ Redis caching for near-zero latency  
- 🗣️ Google TTS/STT integration for speech processing  
- 🤖 Gemini 2.0 Flash integration for advanced AI dialogue generation  
- 🖥️ FastAPI backend + React frontend for scalable deployment  

## ⚙️ Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/yourusername/tamul_ai.git
   cd tamul_ai
   ```

2. **Backend Setup**
   a. Create a virtual environment

   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

   b. Install Python dependencies

   ```bash
   pip install -r requirements.txt
   ```

   c. Ensure Redis is installed and running

   * **Linux (Debian/Ubuntu)**:

     ```bash
     sudo apt update
     sudo apt install redis-server
     sudo service redis-server start
     ```
   * **macOS (Homebrew)**:

     ```bash
     brew install redis
     brew services start redis
     ```
   * **Windows**:
     Use [Memurai](https://www.memurai.com/) or install Redis via WSL.

3. **Frontend Setup**

   ```bash
   cd frontend
   npm install
   npm start
   ```

   The React dev server runs at [http://localhost:3000](http://localhost:3000).

4. **Running the Backend Server**

   ```bash
   cd ..
   uvicorn app.app:app --host 0.0.0.0 --port 8000 --reload
   ```

   * API: [http://localhost:8000](http://localhost:8000)
   * Docs: [http://localhost:8000/docs](http://localhost:8000/docs)

## 🔗 Integrations

* **Google TTS/STT** – real-time speech generation & transcription
* **Gemini 2.0 Flash** – advanced AI dialogue generation
* **Redis** – ultra-fast caching & task queue management

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss.

## 📜 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## 💡 Author

**Tamul AI Team**

---

> For Docker, Nginx deployment, and production best practices, check the upcoming [docs](docs/README.md).

```
```
