# workflows/hotfix.md

# Hotfix Workflow

> Workflow dành cho các sự cố nghiêm trọng trên Production cần được xử lý ngay lập tức.

---

# 1. Overview

## Purpose

Hotfix Workflow được sử dụng khi Production gặp sự cố nghiêm trọng cần được khắc phục ngay để giảm thiểu ảnh hưởng tới người dùng hoặc doanh nghiệp.

Ví dụ:

- Website không truy cập được
- API trả về 500
- Không thể thanh toán
- Không thể đăng nhập
- Rò rỉ dữ liệu
- Security Vulnerability

Khác với Feature Development hoặc Bug Fix, Hotfix ưu tiên:

- Khôi phục hệ thống nhanh nhất
- Giảm downtime
- Giảm phạm vi thay đổi
- Có thể rollback nhanh

---

# 2. Objectives

Workflow phải đảm bảo:

- Khôi phục Production nhanh nhất
- Patch nhỏ nhất có thể
- Có khả năng Rollback
- Có kiểm thử tối thiểu
- Theo dõi sau Release

---

# 3. Participants

| Agent | Responsibility |
|---------|---------------|
| Incident Agent | Phân loại sự cố |
| Bug Analysis Agent | Phân tích nguyên nhân |
| Developer Agent | Tạo Patch |
| Review Agent | Review nhanh |
| Tester Agent | Smoke Test |
| Release Agent | Deploy Hotfix |
| Monitoring Agent | Theo dõi sau Release |

---

# 4. Trigger

Workflow được kích hoạt khi:

- Production Incident
- Monitoring Alert
- Security Alert
- Customer Escalation
- Critical Bug

---

# 5. Severity

| Severity | Description |
|----------|-------------|
| Critical | Hệ thống ngừng hoạt động |
| High | Chức năng chính không sử dụng được |
| Medium | Một phần chức năng lỗi |
| Low | Không ảnh hưởng lớn |

Chỉ Severity Critical và High mới kích hoạt Hotfix Workflow.

---

# 6. Input

Workflow nhận:

```
Incident Report

↓

Logs

↓

Metrics

↓

Alert

↓

Stack Trace

↓

Production Configuration
```

---

# 7. Output

Workflow tạo:

```
Root Cause Report

↓

Hotfix Patch

↓

Smoke Test Report

↓

Deployment Report

↓

Postmortem Report
```

---

# 8. High Level Flow

```
Incident

↓

Analysis

↓

Root Cause

↓

Patch

↓

Review

↓

Smoke Test

↓

Deploy

↓

Monitoring

↓

Close Incident
```

---

# 9. Step 1 - Incident Analysis

Incident Agent xác định:

- Severity
- Impact
- Affected Users
- Business Impact
- SLA

Output:

```
Incident Artifact
```

---

# 10. Step 2 - Root Cause Analysis

Bug Analysis Agent thực hiện:

- Đọc Logs
- Đọc Metrics
- Đọc Stack Trace
- Đọc Recent Changes

Không đọc toàn bộ Repository.

Output:

```
Root Cause Artifact
```

---

# 11. Step 3 - Generate Hotfix

Developer Agent:

```
Root Cause

↓

Context Engine

↓

Capability

↓

Skill

↓

LLM

↓

Patch
```

Yêu cầu:

- Thay đổi nhỏ nhất
- Không Refactor
- Không thêm Feature

---

# 12. Step 4 - Review

Review Agent kiểm tra:

- Patch đúng phạm vi
- Không ảnh hưởng chức năng khác
- Có thể Rollback
- Không tạo Security Risk

Review chỉ tập trung vào Hotfix.

---

# 13. Step 5 - Smoke Test

Tester Agent thực hiện:

- Smoke Test
- Critical Path Test
- Health Check

Không cần chạy toàn bộ Regression nếu thời gian không cho phép.

---

# 14. Step 6 - Deploy

Release Agent:

- Build
- Deploy
- Verify Deployment
- Update Version
- Generate Release Note

---

# 15. Step 7 - Monitoring

Monitoring Agent theo dõi:

- Error Rate
- Response Time
- CPU
- Memory
- User Sessions
- Alert

Nếu phát hiện bất thường:

```
Rollback
```

---

# 16. Rollback Strategy

Nếu Hotfix thất bại:

```
Deployment

↓

Monitoring Failed

↓

Rollback

↓

Verify

↓

Close Incident
```

Rollback luôn phải được chuẩn bị trước khi Deploy.

---

# 17. Sequence Diagram

```text
Incident
    │
    ▼
Incident Agent
    │
    ▼
Bug Analysis Agent
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
    ▼
Release Agent
    │
    ▼
Monitoring Agent
    │
 ┌──┴───────────┐
 │ Healthy?     │
 └────┬─────────┘
      │
  No  ▼
Rollback
      │
      ▼
Close Incident
```

---

# 18. Quality Gates

| Gate | Condition |
|------|-----------|
| Analysis | Root Cause Identified |
| Patch | Build Success |
| Review | No Critical Issue |
| Smoke Test | Passed |
| Monitoring | Stable |

---

# 19. Best Practices

✅ Patch nhỏ nhất có thể.

✅ Chỉ sửa đúng nguyên nhân.

✅ Luôn có Rollback Plan.

✅ Theo dõi sau Deploy.

✅ Viết Postmortem sau Incident.

---

# 20. Anti-patterns

❌ Refactor trong Hotfix.

❌ Thêm Feature.

❌ Chạy Migration lớn.

❌ Deploy mà không có Monitoring.

❌ Không chuẩn bị Rollback.

---

# 21. Metrics

Theo dõi:

- MTTR (Mean Time To Recovery)
- Downtime
- Deployment Time
- Rollback Count
- Incident Count
- Customer Impact
- Token Usage
- AI Execution Time

---

# 22. Postmortem

Sau khi Incident kết thúc, Workflow phải sinh:

```
Postmortem Report
```

Bao gồm:

- Timeline
- Root Cause
- Impact
- Resolution
- Lessons Learned
- Preventive Actions

---

# 23. Summary

Hotfix Workflow được tối ưu cho các sự cố Production có mức độ nghiêm trọng cao.

Mục tiêu chính là:

- Khôi phục dịch vụ nhanh nhất
- Giảm rủi ro khi triển khai
- Có khả năng Rollback
- Theo dõi sau Release
- Lưu đầy đủ Artifact để phục vụ Postmortem và cải tiến hệ thống