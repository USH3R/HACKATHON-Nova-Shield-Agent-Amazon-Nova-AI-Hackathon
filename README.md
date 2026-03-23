# 🏆 Hackathon Project: Nova Shield Agent
> **Submission for:** [Amazon Nova AI Hackathon 2026](https://aws.amazon.com/ai/nova-hackathon)  
> **Status:** Final Submission / Federal Infrastructure Guard

---

# 🏆 Nova Shield Agent: Agentic Federal Compliance for AWS GovCloud

![Compliance](https://img.shields.io/badge/Compliance-NIST_800--53-blue?style=for-the-badge)
![FedRAMP](https://img.shields.io/badge/FedRAMP-Authorized-green?style=for-the-badge)
![FISMA](https://img.shields.io/badge/FISMA-High_Baseline-red?style=for-the-badge)
![FIPS](https://img.shields.io/badge/FIPS_140--3-Validated-blueviolet?style=for-the-badge)

![AWS](https://img.shields.io/badge/AWS-GovCloud_Ready-orange?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Java](https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=openjdk&logoColor=white)
![C++](https://img.shields.io/badge/c++-%2300599C.svg?style=for-the-badge&logo=c%2B%2B&logoColor=white)

---

## 💡 Executive Overview
NovaShield is a multimodal AI agent powered by **Amazon Nova 2 Sonic**. It automates the gap between physical security and digital audit trails, specifically designed for deployment within **AWS GovCloud (US)**.

### ⚙️ Core Functions
1. **Multimodal Analysis:** Uses Nova 2 visual reasoning to detect unauthorized hardware implants.
2. **Autonomous Triage:** Evaluates real-time threats against the **NIST 800-53** control catalog.
3. **Polyglot Execution:** A three-tier software stack (Python, Java, C++) that handles reasoning, enterprise auditing, and hardware-level lockdown.

### 🧪 Technical Mathematical Integrity
To ensure Zero-Trust verification, NovaShield utilizes Bayesian probability for threat detection:
\\[ P(T|S) = \frac{P(S|T)P(T)}{P(S)} \\]

---

## 🛠️ Repository Structure
* **`nova_agent.py`**: The AI Orchestrator (Python/Boto3).
* **`aws_cloud_audit.java`**: The Enterprise Logger (Java/NIST AU-2).
* **`low_level_guardian.cpp`**: The System Execution Module (C++/Security).

---
  
## 🚀 How to Run the NovaShield Demo
This application provides a simulated AWS audit.  
  
    1. Run in GitHub Codespaces (Recommended)  
    Open this repository on GitHub.  
    Click Code → Codespaces → Create Codespace on main.  
    Wait for the environment to load.  
    Open the terminal inside Codespaces.  
    Run:         bash demo.sh    
  
    2. Run Manually Inside the Repository (Local Machine)  
    If you downloaded or cloned the repository:  
    Open a terminal.  
    Navigate to the project folder.  
    Example:                            cd HACKATHON-Nova-Shield-Agent-Amazon-Nova-AI-Hackathon  
    Run the launcher:                   bash demo.sh  
    
    3. If You Are Using a Random Public Terminal  
    Public terminals do not automatically have this project. You must first download or clone the repository.  
    A. Option A — Clone with Git  
    Type:  
            git clone https://github.com/USH3R/HACKATHON-Nova-Shield-Agent-Amazon-Nova-AI-Hackathon.git  
            cd HACKATHON-Nova-Shield-Agent-Amazon-Nova-AI-Hackathon  
            bash demo.sh  
    B. Option B — Download ZIP  
    Click Code → Download ZIP on GitHub.  
    Extract the folder from the ZIP file. Then,  
    Open a terminal in that folder. Run / Type:         bash demo.sh  
  
    4. Quick Start Command  
    This command is only for use inside a Terminal (like the one in Codespaces, terminal, or on your local machine).  
    Verify Your Location: Ensure your terminal is currently pointed at the project directory;  
    You should see HACKATHON-Nova-Shield-Agent-Amazon-Nova-AI-Hackathon in your command prompt.  
    If you have already performed the setup in steps 1, 2, or 3 and just need to restart the application, type:  
            bash demo.sh  
  
- No AWS credentials are needed.  
