import json

def explain_change(change):
    return f"""Change Evidence Summary
----------------------
Tests: {change['tests']}
Security Scan: {change['security_scan']}
Policy Compliance: {change['policy_compliance']}
Approved By: {change['approver']}
"""
