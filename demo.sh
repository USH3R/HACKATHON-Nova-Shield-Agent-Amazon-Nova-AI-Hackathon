#!/bin/bash
echo "=== NOVASHIELD GOV-CLOUD AUDIT START ==="
python3 run.py
echo "[+] Audit Report Generated: audit_report.json"
echo "[+] Remediation Plan: See reports/remediate_s3.sh"
echo "=== NOVASHIELD AUDIT COMPLETE ==="
