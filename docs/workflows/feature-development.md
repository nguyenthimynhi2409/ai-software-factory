# workflows/feature-development.md

# Feature Development Workflow

> Workflow chuẩn để phát triển một tính năng mới trong AI Software Factory.

---

# 1. Overview

## Purpose

Feature Development Workflow chịu trách nhiệm tự động hóa toàn bộ quá trình phát triển một chức năng mới.

Workflow bắt đầu từ Requirement và kết thúc khi Feature được Release.

```
Requirement

↓

Planning

↓

Architecture

↓

Development

↓

Review

↓

Testing

↓

Release

↓

Production
```

---

# 2. Objectives

Workflow phải đảm bảo:

- Feature đáp ứng Requirement
- Không làm hỏng chức năng hiện có
- Có Code Review
- Có Testing
- Có Retry khi lỗi
- Có đầy đủ Artifact
- Có thể Audit

---

# 3. Participants

Workflow bao gồm các Agent sau.

| Agent | Responsibility |
|---------|---------------|
| Requirement Agent | Phân tích Requirement |
| Planner Agent | Chia Task |
| Architect Agent | Thiết kế |
| Developer Agent | Sinh Code |
| Review Agent | Review Source |
| Tester Agent | Test |
| Bug Fix Agent | Fix Bug |
| Release Agent | Release |

---

# 4. Input

Workflow nhận:

```
Requirement Artifact
```

Ví dụ

```yaml
feature:
    Add User Login

business_goal:
    User can login using Email

priority:
    High

acceptance_criteria:

- Email required

- Password required

- Remember login

- Lock account after 5 failures
```

---

# 5. Output

Workflow tạo:

```
Requirement

↓

Architecture

↓

Tasks

↓

Source Code

↓

Review Report

↓

Test Report

↓

Release Note
```

---

# 6. High Level Flow

```
┌─────────────┐
│ Requirement │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Requirement │
│ Agent       │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Planner     │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Architect   │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Developer   │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Reviewer    │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Tester      │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Release     │
└─────────────┘
```

---

# 7. Detailed Workflow

## Step 1 - Requirement Analysis

Agent

```
Requirement Agent
```

Input

```
Requirement
```

Output

```
Requirement Artifact
```

Validation

- Business Goal rõ ràng
- Acceptance Criteria đầy đủ
- Không còn ambiguity

Nếu thiếu

```
Ask Clarification
```

---

## Step 2 - Task Planning

Agent

```
Planner Agent
```

Output

```
Task List
```

Ví dụ

```
Task 1

Create Login API

Task 2

Create Login Page

Task 3

Unit Test

Task 4

E2E Test
```

---

## Step 3 - Architecture

Agent

```
Architect Agent
```

Output

```
Architecture Artifact
```

Bao gồm

- API
- Database
- UI
- Sequence
- Dependency

---

## Step 4 - Development

Agent

```
Developer Agent
```

Developer Agent thực hiện:

```
Read Context

↓

Choose Capability

↓

Choose Skill

↓

Generate Prompt

↓

LLM

↓

Validate

↓

Code Artifact
```

Không được đọc toàn bộ repository.

---

## Step 5 - Code Review

Agent

```
Review Agent
```

Kiểm tra:

- Coding Standard
- Naming
- Architecture
- Security
- Performance
- Maintainability
- Duplicate Code

Output

```
Review Report
```

Nếu Fail

```
Developer Agent
```

---

## Step 6 - Testing

Agent

```
Tester Agent
```

Tester tạo:

- Unit Test
- Integration Test
- Playwright
- Regression Test

Output

```
Test Report
```

---

## Step 7 - Bug Fix

Nếu Test Fail

```
Tester

↓

Bug Report

↓

Bug Fix Agent

↓

Patch

↓

Retest
```

Có thể lặp nhiều lần.

---

## Step 8 - Release

Agent

```
Release Agent
```

Kiểm tra

- Review Pass
- Test Pass
- Build Pass
- Version
- Changelog

Output

```
Release Note
```

---

# 8. Sequence Diagram

```text
Requirement

│

▼

Requirement Agent

│

▼

Planner Agent

│

▼

Architect Agent

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

┌──────────────┐
│ Test Failed? │
└──────┬───────┘
       │
   Yes ▼
 Bug Fix Agent
       │
       ▼
   Tester Agent
       │
   No ▼
Release Agent
       │
       ▼
Production
```

---

# 9. Artifact Flow

```
Requirement

↓

Requirement Artifact

↓

Task Artifact

↓

Architecture Artifact

↓

Source Artifact

↓

Review Artifact

↓

Test Artifact

↓

Release Artifact
```

---

# 10. Quality Gates

Workflow chỉ được chuyển bước khi vượt qua Quality Gate.

| Gate | Condition |
|-------|-----------|
| Requirement | Requirement Complete |
| Planning | Task Complete |
| Development | Build Success |
| Review | No Critical Issue |
| Testing | All Test Passed |
| Release | Approval Completed |

---

# 11. Retry Strategy

Nếu Development thất bại

```
Developer

↓

Retry

↓

Review
```

Nếu Review thất bại

```
Review

↓

Developer
```

Nếu Test thất bại

```
Testing

↓

Bug Fix

↓

Testing
```

Retry tối đa có thể được cấu hình.

---

# 12. Failure Handling

Workflow dừng khi:

- Requirement không hợp lệ
- Build thất bại liên tục
- Review không đạt sau N lần
- Test thất bại sau N lần
- Release bị từ chối

Workflow sinh Failure Artifact để phục vụ phân tích.

---

# 13. Metrics

Workflow nên ghi nhận:

- Lead Time
- Cycle Time
- Retry Count
- Number of Bugs
- Review Score
- Test Coverage
- Token Usage
- LLM Cost
- Execution Time

Các chỉ số này giúp tối ưu hiệu suất của AI Software Factory.

---

# 14. Best Practices

✅ Mỗi Agent chỉ thực hiện một trách nhiệm.

✅ Chỉ truyền Artifact giữa các Agent.

✅ Context được tải theo nhu cầu (Lazy Loading).

✅ Review luôn diễn ra trước Testing.

✅ Không bỏ qua Quality Gate.

---

# 15. Anti-patterns

❌ Developer Agent tự Release.

❌ Tester Agent sửa Code.

❌ Review Agent viết lại Requirement.

❌ Đọc toàn bộ Repository.

❌ Một Agent đảm nhiệm toàn bộ Workflow.

---

# 16. Summary

Feature Development Workflow là workflow quan trọng nhất của AI Software Factory.

Nó điều phối toàn bộ quá trình từ Requirement đến Production thông qua các Agent chuyên biệt, sử dụng Artifact làm đầu ra trung gian và Quality Gate để đảm bảo chất lượng ở từng bước.

Workflow này là nền tảng để mở rộng sang các workflow khác như Bug Fix, Hotfix, Refactor và Release.