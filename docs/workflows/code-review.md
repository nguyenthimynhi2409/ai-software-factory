# workflows/code-review.md

# Code Review Workflow

> Workflow chuẩn để đánh giá chất lượng mã nguồn và các Artifact trước khi chuyển sang Testing hoặc Release.

---

# 1. Overview

## Purpose

Code Review Workflow đảm bảo rằng mọi thay đổi đều đáp ứng tiêu chuẩn kỹ thuật, kiến trúc và chất lượng trước khi được tích hợp vào hệ thống.

Workflow này **không sửa code**.

Workflow chỉ:

- Phân tích
- Đánh giá
- Đưa ra nhận xét
- Phát hiện rủi ro
- Đề xuất cải thiện
- Quyết định Pass hoặc Reject

Nếu Review thất bại, Workflow sẽ trả Artifact về Developer Workflow.

---

# 2. Objectives

Workflow phải đảm bảo:

- Code đúng Requirement
- Không vi phạm Coding Standard
- Không tạo Technical Debt
- Không ảnh hưởng kiến trúc
- Không tạo Security Risk
- Có Maintainability tốt
- Có Performance phù hợp

---

# 3. Participants

| Agent | Responsibility |
|---------|---------------|
| Review Agent | Điều phối quá trình review |
| Static Analysis Agent | Phân tích source code |
| Architecture Review Agent | Kiểm tra kiến trúc |
| Security Review Agent | Kiểm tra bảo mật |
| Performance Review Agent | Kiểm tra hiệu năng |
| Documentation Agent | Sinh báo cáo review |

---

# 4. Trigger

Workflow được kích hoạt khi:

- Developer hoàn thành Feature
- Developer hoàn thành Bug Fix
- Pull Request được tạo
- Merge Request được tạo
- Refactor hoàn thành

---

# 5. Input

Workflow nhận:

```
Requirement Artifact

↓

Architecture Artifact

↓

Source Artifact

↓

Coding Standard

↓

Design Rules

↓

Test Cases
```

---

# 6. Output

Workflow tạo:

```
Review Report

↓

Issue List

↓

Improvement Suggestions

↓

Approval Status
```

---

# 7. High Level Flow

```
Collect Artifacts

↓

Static Analysis

↓

Architecture Review

↓

Security Review

↓

Performance Review

↓

Generate Report

↓

Approve / Reject
```

---

# 8. Step 1 - Collect Context

Review Agent thu thập:

- Requirement
- Architecture
- Source Code
- Coding Standard
- Related Files
- Previous Review

Không đọc toàn bộ Repository.

---

# 9. Step 2 - Static Analysis

Static Analysis Agent kiểm tra:

- Naming Convention
- Formatting
- Unused Code
- Duplicate Code
- Dead Code
- Complexity
- Lint Issues

Output

```
Static Analysis Report
```

---

# 10. Step 3 - Requirement Compliance

Review Agent xác minh:

- Code có đáp ứng Requirement?
- Có thiếu Acceptance Criteria?
- Có xử lý Edge Cases?
- Có Business Logic sai?

Output

```
Requirement Review
```

---

# 11. Step 4 - Architecture Review

Architecture Review Agent kiểm tra:

- Layer Violation
- Dependency Direction
- Module Boundary
- SOLID
- Clean Architecture
- Design Pattern

Output

```
Architecture Report
```

---

# 12. Step 5 - Security Review

Security Review Agent kiểm tra:

- SQL Injection
- XSS
- CSRF
- Authentication
- Authorization
- Sensitive Data Exposure
- Hardcoded Secret

Output

```
Security Report
```

---

# 13. Step 6 - Performance Review

Performance Review Agent kiểm tra:

- Large Loop
- Memory Usage
- N+1 Query
- Duplicate API Calls
- Unnecessary Rendering
- Expensive Computation

Output

```
Performance Report
```

---

# 14. Step 7 - Maintainability Review

Kiểm tra:

- Readability
- Modularity
- Reusability
- Testability
- Documentation
- Comments

Output

```
Maintainability Report
```

---

# 15. Step 8 - Generate Review Report

Documentation Agent tổng hợp:

```
Static Report

+

Architecture Report

+

Security Report

+

Performance Report

+

Maintainability Report

↓

Review Report
```

---

# 16. Review Decision

Workflow đưa ra:

| Status | Meaning |
|----------|----------|
| Approved | Được phép tiếp tục |
| Approved with Comment | Được tiếp tục nhưng cần cải thiện |
| Changes Requested | Trả về Developer |
| Rejected | Không đạt yêu cầu |

---

# 17. Quality Gates

Workflow chỉ Pass khi:

| Gate | Condition |
|------|-----------|
| Requirement | Passed |
| Static Analysis | Passed |
| Architecture | Passed |
| Security | Passed |
| Performance | Passed |
| Maintainability | Passed |

---

# 18. Artifact Flow

```
Requirement Artifact

↓

Source Artifact

↓

Static Analysis Report

↓

Architecture Report

↓

Security Report

↓

Performance Report

↓

Review Report
```

---

# 19. Sequence Diagram

```text
Developer Workflow
        │
        ▼
Review Agent
        │
        ▼
Static Analysis Agent
        │
        ▼
Architecture Review Agent
        │
        ▼
Security Review Agent
        │
        ▼
Performance Review Agent
        │
        ▼
Documentation Agent
        │
   ┌────┴──────────┐
   │ Review Pass ? │
   └────┬──────────┘
        │
 No     ▼
Developer Workflow
        │
 Yes    ▼
Testing Workflow
```

---

# 20. Metrics

Theo dõi:

- Review Duration
- Critical Issues
- Major Issues
- Minor Issues
- Maintainability Score
- Security Score
- Performance Score
- Review Pass Rate
- AI Token Usage

---

# 21. Best Practices

✅ Review theo Requirement trước.

✅ Review Architecture trước Coding Style.

✅ Chỉ review phần thay đổi.

✅ Luôn kiểm tra Security.

✅ Luôn tạo Review Report.

✅ Mọi Issue phải gắn với bằng chứng cụ thể.

---

# 22. Anti-patterns

❌ Chỉ review Coding Style.

❌ Bỏ qua Requirement.

❌ Bỏ qua Security.

❌ Review toàn bộ Repository.

❌ Không giải thích lý do Reject.

---

# 23. Integration

Workflow thường nằm giữa Development và Testing.

```
Requirement

↓

Planning

↓

Development

↓

Code Review

↓

Testing

↓

Release
```

---

# 24. Summary

Code Review Workflow là Quality Gate quan trọng trong AI Software Factory.

Workflow không sửa code mà tập trung vào việc đánh giá toàn diện chất lượng của Source Code và các Artifact liên quan. Kết quả của Workflow là Review Report và Approval Status, làm cơ sở để quyết định chuyển sang Testing hay trả về Development.

Code Review giúp giảm Technical Debt, tăng Maintainability và đảm bảo chất lượng hệ thống trước khi phát hành.