# workflows/refactor.md

# Refactor Workflow

> Workflow chuẩn để cải thiện chất lượng source code mà không làm thay đổi hành vi của hệ thống.

---

# 1. Overview

## Purpose

Refactor Workflow được sử dụng khi cần:

- Cải thiện chất lượng source code
- Giảm Technical Debt
- Chuẩn hóa Coding Style
- Đơn giản hóa Logic
- Tăng khả năng Maintainability
- Tăng Performance (không thay đổi Business Logic)

Refactor Workflow **không được phép thay đổi hành vi của hệ thống**.

---

# 2. Objectives

Workflow phải đảm bảo:

- Business Behavior không đổi
- Public API không đổi (trừ khi có kế hoạch Migration)
- Test vẫn Pass
- Giảm Technical Debt
- Tăng Maintainability

---

# 3. Trigger

Workflow được kích hoạt khi:

- Code Smell Detection
- SonarQube Issue
- Large File
- Duplicate Code
- Long Function
- Cyclomatic Complexity cao
- Manual Request

---

# 4. Participants

| Agent | Responsibility |
|---------|---------------|
| Analysis Agent | Phân tích Code Smell |
| Refactor Agent | Đề xuất Refactor |
| Review Agent | Review Refactor |
| Tester Agent | Regression Test |
| Documentation Agent | Cập nhật tài liệu |

---

# 5. Input

Workflow nhận:

```
Source Code

↓

Architecture

↓

Coding Standard

↓

Test Cases
```

---

# 6. Output

Workflow tạo:

```
Refactor Plan

↓

Updated Source Code

↓

Review Report

↓

Regression Report

↓

Documentation Update
```

---

# 7. High Level Flow

```
Analyze

↓

Identify Code Smell

↓

Create Refactor Plan

↓

Apply Refactor

↓

Review

↓

Regression Test

↓

Documentation
```

---

# 8. Step 1 - Analyze Source Code

Analysis Agent phân tích:

- Duplicate Code
- Long Method
- Large Class
- Deep Nesting
- Magic Number
- Dead Code
- Unused Dependency
- Naming Issues

Output

```
Code Smell Report
```

---

# 9. Step 2 - Prioritize Refactor

Không phải mọi Code Smell đều cần sửa.

AI đánh giá:

- Business Impact
- Risk
- Complexity
- Cost
- Expected Benefit

Output

```
Refactor Plan
```

---

# 10. Step 3 - Context Retrieval

Context Engine chỉ tải:

```
Affected Files

↓

Related Classes

↓

Dependencies

↓

Tests
```

Không đọc toàn bộ Repository.

---

# 11. Step 4 - Apply Refactor

Refactor Agent chọn Capability phù hợp:

```
Extract Method

Rename

Extract Interface

Move Class

Remove Duplication

Simplify Logic

Optimize Structure
```

Output

```
Source Artifact
```

---

# 12. Step 5 - Code Review

Review Agent kiểm tra:

- Coding Standard
- Readability
- Architecture
- Maintainability
- Performance
- Behavior Change

Nếu phát hiện thay đổi Business Logic:

```
Reject Refactor
```

---

# 13. Step 6 - Regression Test

Tester Agent thực hiện:

- Unit Test
- Integration Test
- Regression Test

Yêu cầu:

```
Behavior Before

=

Behavior After
```

---

# 14. Step 7 - Documentation

Documentation Agent cập nhật:

- Class Diagram
- Sequence Diagram
- Architecture Document
- ADR (nếu cần)

---

# 15. Artifact Flow

```
Code Smell Report

↓

Refactor Plan

↓

Updated Source

↓

Review Report

↓

Regression Report

↓

Documentation
```

---

# 16. Sequence Diagram

```text
Source Code
      │
      ▼
Analysis Agent
      │
      ▼
Refactor Agent
      │
      ▼
Review Agent
      │
      ▼
Tester Agent
      │
 ┌────┴────────────┐
 │ Tests Passed ?  │
 └────┬────────────┘
      │
 No   ▼
Refactor Agent
      │
 Yes  ▼
Documentation Agent
      │
      ▼
Completed
```

---

# 17. Refactor Patterns

Framework nên hỗ trợ:

- Extract Method
- Extract Class
- Extract Interface
- Rename Variable
- Rename Function
- Replace Conditional with Strategy
- Remove Dead Code
- Remove Duplication
- Dependency Injection
- Simplify Boolean Expression

---

# 18. Quality Gates

| Gate | Condition |
|------|-----------|
| Analysis | Code Smell Identified |
| Refactor | Build Success |
| Review | No Architecture Issue |
| Testing | Regression Passed |
| Documentation | Updated |

---

# 19. Metrics

Theo dõi:

- Number of Code Smells Removed
- Cyclomatic Complexity
- Maintainability Index
- Technical Debt Reduction
- LOC Changed
- Review Score
- Test Coverage

---

# 20. Best Practices

✅ Refactor từng bước nhỏ.

✅ Chạy Test sau mỗi lần Refactor.

✅ Không kết hợp Feature Development.

✅ Luôn Review.

✅ Cập nhật Documentation.

---

# 21. Anti-patterns

❌ Refactor và thêm Feature cùng lúc.

❌ Refactor khi chưa có Test.

❌ Refactor quá nhiều module trong một lần.

❌ Đổi Business Logic.

❌ Xóa Code mà không xác minh.

---

# 22. Summary

Refactor Workflow giúp AI Software Factory cải thiện chất lượng mã nguồn theo cách có kiểm soát.

Workflow tập trung vào việc giảm Technical Debt, tăng Maintainability và giữ nguyên hành vi của hệ thống thông qua Review, Regression Test và Documentation.