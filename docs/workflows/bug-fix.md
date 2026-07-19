# workflows/bug-fix.md

# Bug Fix Workflow

> Workflow chuẩn để phân tích, xác định nguyên nhân và sửa lỗi phần mềm.

---

# 1. Overview

## Purpose

Bug Fix Workflow được sử dụng khi hệ thống phát hiện lỗi trong quá trình:

- Testing
- Production
- UAT
- Code Review
- Monitoring

Workflow giúp AI:

- Phân tích nguyên nhân
- Khoanh vùng phạm vi ảnh hưởng
- Sinh bản vá (Patch)
- Đảm bảo không phát sinh lỗi mới

---

# 2. Objectives

Workflow phải đảm bảo:

- Tìm đúng nguyên nhân gốc (Root Cause)
- Chỉ sửa phần cần thiết
- Không làm ảnh hưởng chức năng khác
- Có Regression Test
- Có Review trước khi Merge

---

# 3. Participants

| Agent | Responsibility |
|---------|---------------|
| Bug Analysis Agent | Phân tích lỗi |
| Developer Agent | Sinh Patch |
| Review Agent | Review Patch |
| Tester Agent | Regression Test |
| Release Agent | Release Hotfix hoặc Merge |

---

# 4. Trigger

Workflow được kích hoạt khi có:

- Test Failed
- Production Incident
- Monitoring Alert
- User Report
- QA Report
- Security Finding

---

# 5. Input

Workflow nhận các Artifact sau.

```
Bug Report

↓

Stack Trace

↓

Log

↓

Source Code

↓

Test Report

↓

Requirement
```

Ví dụ

```yaml
title: Login Failed

environment: Production

severity: High

steps:

- Open Login Page

- Input Email

- Click Login

expected:

Login Success

actual:

500 Internal Server Error
```

---

# 6. Output

Workflow sinh ra

```
Root Cause Report

↓

Patch

↓

Review Report

↓

Regression Report

↓

Release Note
```

---

# 7. High Level Workflow

```
Bug Report

↓

Analysis

↓

Locate Root Cause

↓

Generate Patch

↓

Review

↓

Regression Test

↓

Release
```

---

# 8. Step 1 - Bug Analysis

Agent

```
Bug Analysis Agent
```

Input

- Bug Report
- Logs
- Stack Trace
- Source Code

Output

```
Root Cause Artifact
```

Agent cần xác định:

- Điều kiện gây lỗi
- Thành phần bị ảnh hưởng
- Mức độ ảnh hưởng
- Phạm vi sửa

---

# 9. Step 2 - Context Retrieval

Không đọc toàn bộ repository.

Context Engine chỉ tải:

```
Related Files

↓

Dependencies

↓

Recent Commits

↓

Relevant Tests

↓

Business Rules
```

---

# 10. Step 3 - Root Cause Analysis

Ví dụ

```
Null Pointer

↓

Missing Validation

↓

API Changed

↓

Database Schema Changed

↓

Configuration Error
```

Root Cause phải được lưu thành Artifact.

---

# 11. Step 4 - Patch Generation

Developer Agent thực hiện

```
Read Root Cause

↓

Choose Capability

↓

Choose Skill

↓

Generate Prompt

↓

LLM

↓

Patch
```

Patch phải càng nhỏ càng tốt.

---

# 12. Step 5 - Review

Review Agent kiểm tra

- Root Cause đúng chưa?
- Patch có đúng phạm vi?
- Có tạo Duplicate Logic?
- Có vi phạm Coding Standard?
- Có gây Security Risk?

Output

```
Review Report
```

Nếu Fail

```
Developer Agent
```

---

# 13. Step 6 - Regression Test

Tester Agent thực hiện

```
Regression Test

↓

Smoke Test

↓

Affected Area Test

↓

Integration Test
```

Output

```
Regression Report
```

---

# 14. Step 7 - Release

Release Agent kiểm tra

- Patch Approved
- Regression Passed
- Version Updated
- Release Note Generated

Sau đó Merge vào Branch phù hợp.

---

# 15. Artifact Flow

```
Bug Report

↓

Root Cause

↓

Patch

↓

Review Report

↓

Regression Report

↓

Release Note
```

---

# 16. Sequence Diagram

```text
Bug Report
     │
     ▼
Bug Analysis Agent
     │
     ▼
Context Engine
     │
     ▼
Developer Agent
     │
     ▼
Review Agent
     │
     ▼
Tester Agent
     │
 ┌───┴───────────┐
 │ Regression OK?│
 └──────┬────────┘
        │
  No    ▼
 Bug Fix Agent
        │
        ▼
 Developer Agent
        │
  Yes   ▼
 Release Agent
```

---

# 17. Quality Gates

| Gate | Condition |
|------|-----------|
| Analysis | Root Cause Identified |
| Patch | Build Success |
| Review | No Critical Issue |
| Regression | All Tests Passed |
| Release | Approved |

---

# 18. Retry Policy

Analysis Failed

↓

Retry Analysis

Developer Failed

↓

Retry Patch

Review Failed

↓

Developer

Regression Failed

↓

Developer

Mỗi bước có thể cấu hình số lần Retry.

---

# 19. Failure Handling

Workflow dừng khi:

- Không xác định được Root Cause
- Patch không Build được
- Review thất bại nhiều lần
- Regression liên tục thất bại

Workflow sinh:

```
Failure Artifact
```

để phục vụ phân tích sau này.

---

# 20. Metrics

Theo dõi các chỉ số:

- Mean Time To Repair (MTTR)
- Retry Count
- Patch Size
- Number of Files Changed
- Review Score
- Regression Coverage
- AI Token Usage
- AI Execution Time

---

# 21. Best Practices

✅ Luôn xác định Root Cause trước khi sửa.

✅ Chỉ sửa phần liên quan.

✅ Không Refactor trong Bug Fix Workflow.

✅ Luôn Regression Test.

✅ Lưu Root Cause để tái sử dụng.

---

# 22. Anti-patterns

❌ Sửa lỗi mà chưa biết nguyên nhân.

❌ Thay đổi nhiều module không liên quan.

❌ Merge khi chưa Regression.

❌ Dùng Bug Fix Workflow để phát triển Feature mới.

---

# 23. Summary

Bug Fix Workflow tập trung vào việc:

- Phân tích lỗi
- Xác định Root Cause
- Sinh Patch nhỏ nhất có thể
- Đảm bảo không phát sinh Regression
- Release an toàn

Workflow này giúp AI Software Factory xử lý lỗi một cách có kiểm soát và có khả năng kiểm toán thông qua Artifact và Metrics.