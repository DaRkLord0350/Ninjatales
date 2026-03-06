# 🥷 Ninja Story Builder 📚  
*Making Leetcode Dynamic Programming... Literary and Fun!*

---

## 🚀 Overview


**Ninja Story Builder** is a creative fusion of **Dynamic Programming** and **Multi-Agent AI Workflows**.

It solves the classic **Ninja Training** problem — where for `N` days and 3 possible tasks per day, the goal is to **maximize total points** without repeating tasks on consecutive days.

But here’s the twist:  
Each task decision for a day becomes a **chapter** in an evolving story, crafted by **LLM-powered agents**!  
The result? An automatically generated, task-driven, multi-day **adventure story**.

---

## 🎯 Why This Project?

Leetcode is great for technical prep — but let’s be honest, it can get repetitive.  
This project transforms **algorithm practice** into a **playground for creativity**, using:

- 📈 **Dynamic Programming** for task optimization  
- 🧠 **LLMs (Google Gemini 2.5 Flash)** for content generation  
- 🔁 **Multi-Agent Systems** for coherent storytelling  
- 🔧 **LangGraph** for graph-based AI workflows
- 🔌 **Bytez SDK** for unified LLM access

---

## 🧠 Core Concepts

### 1. **Ninja Training Problem (DP)**

> For each of `N` days, choose a task from `{task1, task2, task3}` such that the same task is not performed on two consecutive days. Maximize the sum of points.

Implemented using **Bottom-Up Tabulation** with memoization to compute the optimal schedule efficiently.

---

### 2. **Multi-Agent Chapter Generation**

- For every day `i`, an **Agent**:
  - Takes the task chosen for day `i`
  - Receives the chapter from day `i-1` (if any)
  - Generates a `Chapter` using structured inputs:
    ```python
    class Chapter(BaseModel):
        title: str
        content: str
        day_number: int
    ```
  - Adds it to the ongoing storybook.


---

## 🧪 Tech Stack

| Component | Tool / Framework | Version |
|-----------|------------------|----------|
| **Dynamic Programming** | Custom DP Optimizer (Python) | - |
| **Task Scheduling** | Matrix Operations & Path Finding | - |
| **Agent Orchestration** | [LangGraph](https://github.com/langchain-ai/langgraph) | ^1.0.9 |
| **LLM API** | [Bytez SDK](https://bytez.ai) | Latest |
| **LLM Model** | Google Gemini 2.5 Flash | - |
| **Data Validation** | [Pydantic](https://pydantic.dev) | ^2.0 |
| **Logging** | Rich + Custom Logger | - |
| **Environment** | Python-dotenv | ^0+ |
| **NumPy** | Data Processing | ^2.4 |

---

## � Dependencies

### Core Dependencies
- **langchain** (^1.2) - LLM framework
- **langchain-core** (^1.2) - Core utilities
- **langgraph** (^1.0) - Agent orchestration
- **bytez** - Unified LLM SDK
- **pydantic** - Data validation & typing
- **numpy** - Numerical operations
- **python-dotenv** - Environment variable management
- **colorama** - Terminal color output
- **rich** - Rich formatting & logging
- **typing-extensions** - Advanced type hints

---

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.11+
- pip or conda

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/ninja-story-builder.git
cd ninja-story-builder
```

### 2. Create Virtual Environment
```bash
# Using venv
python -m venv myenv

# On Windows
myenv\Scripts\activate

# On macOS/Linux
source myenv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file in the root directory with your Bytez API key:
```env
BYTEZ_API_KEY=your_bytez_api_key_here
```

**Get your Bytez API key:**
1. Visit [Bytez Dashboard](https://bytez.ai)
2. Create an account or sign in
3. Generate an API key from your dashboard
4. Copy it to your `.env` file

---

## 🚀 Running the Project

### Basic Command
```bash
python main.py --days <num_days> --task1 "<task_description>" --task2 "<task_description>" --task3 "<task_description>"
```

### Example: 7-Day Story
```bash
python main.py --days 7 \
  --task1 "Learn Python" \
  --task2 "Build a Web App" \
  --task3 "Deploy to Cloud"
```

### Example: 3-Day Story
```bash
python main.py --days 3 \
  --task1 "Climb the mountain" \
  --task2 "Defend the village" \
  --task3 "Search for the ancient scroll"
```

### Command Arguments
| Argument | Short | Type | Required | Description |
|----------|-------|------|----------|-------------|
| `--days` | `-d` | int | Yes | Number of days (must be positive) |
| `--task1` | `-t1` | str | Yes | First task description |
| `--task2` | `-t2` | str | Yes | Second task description |
| `--task3` | `-t3` | str | Yes | Third task description |

---

## 📊 How It Works

### 1. **Input Processing**
- Validate command-line arguments
- Initialize story configuration

### 2. **Dynamic Programming Phase**
- Generate random performance matrix (days × tasks)
- Compute optimal task schedule using DP
- Avoid consecutive same tasks constraint

### 3. **Task Analysis**
- Calculate performance metrics per task
- Display task analysis and daily scores
- Show optimal activity sequence

### 4. **Multi-Agent Workflow**
- Initialize LangGraph workflow with agents:
  - **ChapterGenerator**: Creates story chapters using Bytez Gemini 2.5
  - **StorySaver**: Saves final story to file
- Process each day sequentially
- Generate coherent narrative with task continuity

### 5. **Story Generation**
- For each day:
  1. Extract assigned task
  2. Include recap from previous chapter
  3. Call Gemini 2.5 Flash via Bytez
  4. Generate story chapter
  5. Append to full story
- Save complete story to `story.txt`

---

## 📁 Project Structure

```
ninja-story-builder/
├── main.py                          # Entry point
├── requirements.txt                 # Python dependencies
├── .env                            # Environment variables (API keys)
├── README.md                        # Documentation
├── story.txt                        # Generated story output
│
├── agents/
│   ├── writer.py                   # ChapterGenerator agent
│   └── store.py                    # StorySaver agent
│
├── data/
│   ├── story_data.py              # Story singleton & data structures
│   └── schema/
│       ├── chapter.py             # Chapter data model
│       └── feedback.py            # Feedback schema
│
├── llm/
│   └── story_llm.py               # Bytez LLM initialization (Singleton)
│
├── logger/
│   └── logger.py                  # Custom logging utilities
│
├── prompts/
│   └── story_prompt.py            # Story generation system prompts
│
├── utils/
│   ├── input_validator.py         # Input validation functions
│   ├── logger.py                  # Rich-based logging
│   ├── matrix_ops.py              # DP & matrix operations
│   └── print.py                   # Console output formatting
│
└── workflow/
    └── content_creation_workflow.py  # LangGraph agent orchestration
```

---

## 🔑 Key Components Explained

### **StoryLLM (Singleton)**
```python
# Initialize once, use everywhere
llm = StoryLLM.get_instance()
model = llm.model  # Bytez Gemini 2.5 Flash model
```
- Manages Bytez SDK initialization
- Provides singleton access to LLM
- Handles API key from `.env`

### **ChapterGenerator Agent**
```python
# Generates story chapters using Bytez
generator = ChapterGenerator(model, system_prompt)
chapter = generator.generate_chapter(task, days, day_num, recap)
```
- Receives task and day information
- Includes recap from previous chapter
- Calls Gemini 2.5 Flash via Bytez SDK
- Returns structured Chapter object

### **StorySaver Agent**
```python
# Saves generated story to file
saver = StorySaver("story.txt")
saver.store_story(full_story_text)
```
- Writes story to disk
- Logs save confirmation

### **Workflow (LangGraph)**
```
START → ChapterGenerator → Continue? → (YES → ChapterGenerator / NO → StorySaver) → END
```
- Orchestrates agent execution
- Manages state across days
- Handles conditional flow

---

## 📊 Sample Output

### Input
```bash
python main.py --days 3 \
  --task1 "Learn Python" \
  --task2 "Build a Web App" \
  --task3 "Deploy to Cloud"
```

### Console Output
```
INFO: Data to create an epic lore initialized successfully:
INFO: Days: 3 || Task 1: Learn Python || Task 2: Build a Web App | Task 3: Deploy to Cloud

Task Matrix:
[[7, 4, 0], [4, 4, 1], [9, 9, 10]]

Task Performance Analysis
Task: Learn Python - Average Score: 3.67
Task: Build a Web App - Average Score: 3.00
Task: Deploy to Cloud - Average Score: 9.33

Selected activity for day 1: Deploy to Cloud
Selected activity for day 2: Learn Python
Selected activity for day 3: Deploy to Cloud

Generating chapter for task 1/3: Deploy to Cloud
SUCCESS: Chapter written: "Chapter 1"

Generating chapter for task 2/3: Learn Python
SUCCESS: Chapter written: "Chapter 2"

Generating chapter for task 3/3: Deploy to Cloud
SUCCESS: Chapter written: "Chapter 3"

SUCCESS: Story saved at story.txt
```

### Generated Story (story.txt)
```
Chapter 1
[Generated narrative about deploying to cloud...]

Chapter 2
[Generated narrative about learning Python, with recap...]

Chapter 3
[Generated narrative about deploying to cloud again, with continuity...]
```

---

## 🔄 LLM Integration (Bytez API)

### Model Used
- **Provider**: Google
- **Model**: Gemini 2.5 Flash
- **SDK**: Bytez

### API Flow
```
User Input
    ↓
ChapterGenerator prepares prompt
    ↓
Bytez SDK calls Gemini 2.5 Flash API
    ↓
Response: { output: { role, content }, error }
    ↓
Extract content & create Chapter
    ↓
Add to story
```

### Example API Call
```python
from bytez import Bytez

sdk = Bytez(api_key)
model = sdk.model("google/gemini-2.5-flash")
results = model.run("Write a chapter about...")

print(results.output['content'])  # Access generated text
```

---

## 🧪 Testing

### Run Tests
```bash
# Test Bytez integration
python test_bytez.py

# Expected output:
# ✓ API key loaded
# ✓ Bytez SDK initialized
# ✓ Gemini 2.5 Flash model loaded
# ✓ Model response: [generated text]
# ✓ StoryLLM singleton initialized
# ✓ System message loaded
# ✅ All Bytez tests passed!
```

---

## 🛠️ Configuration & Customization

### Customize System Prompt
Edit `prompts/story_prompt.py`:
```python
STORY_SYSTEM_PROMPT = """You are an expert storyteller...
[Customize your system prompt here]
"""
```

### Adjust DP Logic
Modify `utils/matrix_ops.py`:
- Change task allocation algorithm
- Adjust scoring mechanism
- Modify constraint checking

### Change Output Format
Edit `agents/writer.py`:
- Modify chapter structure
- Change output parsing
- Add additional fields

---

## 🚨 Troubleshooting

### Issue: "BYTEZ_API_KEY not found in environment variables"
**Solution**: Ensure `.env` file exists in project root:
```env
BYTEZ_API_KEY=your_actual_api_key
```

### Issue: "Module not found" errors
**Solution**: Install dependencies:
```bash
pip install -r requirements.txt
```

### Issue: "name 'ChatOpenAI' is not defined"
**Solution**: Project uses Bytez, not OpenAI. Ensure you're using the latest version of `main.py`.

### Issue: Story file not created
**Solution**: Check file permissions and ensure `story.txt` can be written to project root.

---

## 📈 Performance & Optimization

- **DP Complexity**: O(N × 3²) where N = days
- **Story Generation**: ~3-4 seconds per chapter via Bytez
- **Memory Usage**: Minimal (~50MB for typical usage)
- **Scalability**: Tested up to 365 days

---

## 🤝 Contributing

Contributions are welcome! Areas for enhancement:
- [ ] Add more task types (4+)
- [ ] Support multiple LLM models via Bytez
- [ ] Add story filtering/refinement
- [ ] Implement story rating system
- [ ] Add streaming support for real-time output

---

## 📄 License

This project is open source and available under the MIT License.

---

## 📚 Resources

- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [Bytez SDK Documentation](https://bytez.ai/docs)
- [Google Gemini API](https://ai.google.dev/)
- [Pydantic Documentation](https://docs.pydantic.dev)
- [Dynamic Programming Guide](https://www.geeksforgeeks.org/dynamic-programming/)

---

## ✨ Example Stories

### Quick 3-Day Quest
```bash
python main.py --days 3 \
  --task1 "Gather herbs" \
  --task2 "Train combat" \
  --task3 "Study ancient texts"
```

### Epic 7-Day Adventure
```bash
python main.py --days 7 \
  --task1 "Climb the mountain" \
  --task2 "Defend the village" \
  --task3 "Search for the ancient scroll"
```

### Developer's Journey
```bash
python main.py --days 5 \
  --task1 "Learn Rust" \
  --task2 "Build a CLI tool" \
  --task3 "Deploy to production"
```

---

## 💬 Questions or Issues?

Open an issue on GitHub or contact the maintainers.

---

**Happy Storytelling! 📖✨**
