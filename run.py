import json
import os

def audit_aws_config():
    sample_file = "samples/infrastructure_v1.json"
    report_dir = "reports"
    report_file = os.path.join(report_dir, "audit_report.json")

    # Ensure reports directory exists
    os.makedirs(report_dir, exist_ok=True)

    # Load sample configuration
    if not os.path.exists(sample_file):
        print(f"[ERROR] Sample file {sample_file} not found.")
        return

    with open(sample_file, "r") as f:
        data = json.load(f)

    print("[*] Auditing AWS Config against NIST 800-171...")
    violations = []

    for resource in data.get("resources", []):
        if resource.get("encryption", "").lower() == "none":
            violations.append(f"NON_COMPLIANT: {resource['id']} missing AES-256 Encryption")
        if resource.get("public", "").lower() == "enabled":
            violations.append(f"NON_COMPLIANT: {resource['id']} has Public Access Enabled")

    status = "FAILED" if violations else "PASSED"
    result = {"status": status, "issues": violations, "remediation": "Apply KMS Key & Restrict Public Access"}

    # Write report
    with open(report_file, "w") as f:
        json.dump(result, f, indent=4)

    print(f"[!] Audit Complete. {len(violations)} violations found.")
    for v in violations:
        print(f"    - {v}")

if __name__ == "__main__":
    audit_aws_config()
