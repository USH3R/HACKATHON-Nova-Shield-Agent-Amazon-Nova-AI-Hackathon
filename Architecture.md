# NovaShield Agent Architecture & Threat Model

**Deployment Target:** AWS GovCloud (US) – Federal Environment  
**Compliance:** NIST 800-53 Controls: AU-2, SC-7, SI-4, AC-3  

---

## 1. Python AI Brain – `nova_ai.py`
- **Purpose:** Real-time detection and reasoning using Amazon Nova 2 Sonic (via `boto3`)  
- **Functionality:**  
  - Receives system or IoT data inputs  
  - Generates threat level, detection description, and recommended action  
- **Notes:** Runs locally in demo mode without AWS credentials; `boto3` import is included to indicate real deployment requirements  

---

## 2. Java Cloud Audit – `AWSCloudAudit.java`
- **Purpose:** Enterprise audit logging of AI-detected threats  
- **Functionality:**  
  - Receives alerts from Python AI Brain  
  - Logs timestamp, detector ID, violation type, and NIST control  
  - Designed for secure storage in AWS GovCloud S3 (simulated for demo)  

---

## 3. C++ Guardian – `NovaShieldGuard.cpp`
- **Purpose:** Hardware-level lockdown and mitigation  
- **Functionality:**  
  - Receives flagged ports or system events from AI Brain  
  - Simulates closing vulnerable ports or isolating compromised hardware  
  - Confirms NIST SC-7 enforcement  

---

## 4. Workflow / Data Flow
1. **AI Brain** analyzes system inputs → generates threat report  
2. **Cloud Audit** logs events for compliance and traceability  
3. **C++ Guardian** executes hardware mitigation actions  
4. Optional: feedback loop to AI Brain for continuous monitoring  

---

## 5. Threat Model
- **Adversary Goals:**  
  - Exploit edge devices or cloud infrastructure  
  - Trigger unauthorized access or privilege escalation  
- **Attack Vectors:**  
  - Compromised IoT devices  
  - Unauthorized network traffic  
  - Privilege escalation attempts on cloud resources  
- **Mitigation Layers:**  
  1. Python AI Brain – early detection & reasoning  
  2. Java Cloud Audit – official logging and traceability  
  3. C++ Guardian – hardware-level enforcement  

---
## Notes
- The architecture is designed for **AWS GovCloud US**, suitable for federal deployment.  
- Demo scripts allow reviewers to run locally without AWS credentials, while preserving **fidelity of design**.  
