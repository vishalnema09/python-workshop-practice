# 🐍 Python for DevOps Masterclass — Practical Projects

A hands-on repository for mastering Python from basics to DevOps automation using tools like Flask, AWS (S3), Terraform, and real-time monitoring.

📍 **GitHub Repo:** [vishalnema09/python-workshop-practice](https://github.com/vishalnema09/python-workshop-practice)

---

## 📅 3-Day Learning Timeline (As per Commits)

| Day    | Focus Area                                                                 |
|--------|----------------------------------------------------------------------------|
| Day 1  | Python fundamentals: variables, lists, conditions, loops, and functions    |
| Day 2  | Automated local backup + AWS S3 upload with `boto3`                        |
| Day 3  | Flask-based CPU/RAM monitoring + Terraform automation with Python script  |

---

## 🚀 Highlights

### 🧠 Day 1 – Python Basics

- ✅ Variables, `if-else` conditions
- ✅ Lists and loop operations (`for`, `while`)
- ✅ Custom functions and modular scripting

📁 Files:
- `conditionals.py`
- `loops.py`
- `fun_utils.py`, `utils.py`

---

### 💾 Day 2 – Backup & Cloud Integration

- ✅ Script to create timestamped `.tar.gz` backups of any folder
- ✅ AWS S3 upload of the backup file via `boto3`
- ✅ AWS credentials via `aws configure` or env vars

📁 Files:
- `backup.py` – local backup
- `s3_backup.py` – S3 uploader

---

### 🌐 Day 3 – DevOps with Flask + Terraform

#### ✅ Real-Time System Monitor
- Flask app (`app.py`) showing live CPU & RAM stats via `psutil`
- Auto-refresh using Plotly/HTML refresh
- Web endpoint: `http://localhost:5000/`

#### ✅ Terraform Automation
- Python script to automate:
  - `terraform init`, `plan`, `apply`, and `destroy`
- Useful for provisioning EC2, VPCs, or any IaC resource

📁 Files:
- `flask/app.py`
- `terra_deploy.py`
- Terraform files inside: `terra-automate/terraform/`

---

## 🔧 Setup Instructions

### 🛠️ Clone the Repo

```bash
git clone https://github.com/vishalnema09/python-workshop-practice.git
cd python-workshop-practice


Automate Terraform
python terra_deploy.py


**Install the dependencies:**
cd flask
pip3 install -r requirements.txt

**Run the Flask application:**
python3 app.py

**Open the application in a web browser:**
http://localhost:5000/

**End Result:**
The homepage displays the current CPU and memory usage of the server.