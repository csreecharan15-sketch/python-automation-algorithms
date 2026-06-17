# Algorithmic Problem Solving & Automation Scripting[cite: 1]

A collection of custom Python modules demonstrating fundamental algorithmic implementations, automated file system operations, and structured text parsing using Regular Expressions (Regex). This repository serves as a practical showcase of core programming logic, software engineering principles, and routine workflow automation.[cite: 1]

## 🚀 Key Features

* **Algorithmic Optimization:** High-performance implementations of classic computer science concepts (e.g., $O(\log n)$ Binary Search and $O(n)$ Hash Map optimization for tracking target pairs).[cite: 1]
* **File Processing Automation:** Scripted mechanisms utilizing systematic directory traversal to discover, filter, and track file types recursively across workspaces.[cite: 1]
* **Structured Text Parsing:** Advanced text processing engine engineered with robust Regular Expressions (Regex) to extract, group, and format tabular insights (Timestamp, Severity Level, Message) from raw, unstructured system log strings.[cite: 1]
* **Clean Architectural Practices:** Implements strong type-hinting, strict encapsulation via Python classes, static method utilization, and self-contained execution blocks (`if __name__ == "__main__":`).[cite: 1]

---

## 📂 Core Architecture

The project is structured logically into modular components:[cite: 1]

```text
├── algorithms.py          # Contains fundamental problem-solving logic and data structures
└── automation_tools.py    # Standard utility scripts handling directory crawls and string parsing
```[cite: 1]

### 1. Algorithmic Solver (`algorithms.py`)
Provides reference implementations for critical optimization algorithms:[cite: 1]
* **Binary Search:** Logarithmic search algorithm operating on sorted arrays. Reduces search space by half dynamically at each step.[cite: 1]
* **Two Sum Optimization:** Linear-time algorithm that substitutes a nested $O(n^2)$ loop layout with an optimized $O(n)$ hash map solution to identify values adding up to a designated numerical target.[cite: 1]

### 2. Automation & Parsing Toolkit (`automation_tools.py`)
Fulfills day-to-day administrative and pipeline scripts:[cite: 1]
* **File Automation:** Automates system exploration by safely filtering data across deep folder structures (`os.walk`).[cite: 1]
* **Regex Log Parser:** Tokenizes standardized server log entries into highly queryable JSON/Dictionary formats for analysis or export.[cite: 1]

---

## 💻 Getting Started

### Prerequisites
* Python 3.8 or higher installed on your local machine.[cite: 1]
* Git installed for version control management.[cite: 1]

### Installation & Execution
1. **Clone the repository:**
```bash
   git clone [https://github.com/csreecharan15-sketch/python-automation-algorithms.git](https://github.com/csreecharan15-sketch/python-automation-algorithms.git)
   cd YOUR_REPOSITORY_NAME
   ```[cite: 1]

2. **Execute the Automation and Parsing module:**
```bash
   python automation_tools.py
   ```[cite: 1]

3. **Execute the Algorithms module:**
```bash
   python algorithms.py
   ```[cite: 1]

---

## 🛠️ Version Control Workflow

This repository standardizes modern engineering habits using a clean Git branching model. Key operations used during its lifecycle:[cite: 1]

```bash
# Initialize project and stage elements
git init
git add algorithms.py automation_tools.py README.md

# Log changes with meaningful commit messages
git commit -m "Feat: Add automation toolkit and optimized algorithmic solvers"

# Link to GitHub and establish tracking branch
git branch -M main
git remote add origin [https://github.com/csreecharan15-sketch/python-automation-algorithms.git](https://github.com/csreecharan15-sketch/python-automation-algorithms.git)
git push -u origin main
```[cite: 1]