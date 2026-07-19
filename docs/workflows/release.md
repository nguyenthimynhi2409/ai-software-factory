# workflows/release.md

# Release Workflow

> Workflow chịu trách nhiệm phát hành một phiên bản phần mềm lên môi trường Production.

---

# 1. Overview

## Purpose

Release Workflow đảm bảo rằng một phiên bản phần mềm chỉ được triển khai khi đã vượt qua tất cả các Quality Gate.

Workflow này không viết code.

Workflow chỉ chịu trách nhiệm:

- Verify
- Build
- Package
- Deploy
- Validate
- Monitor
- Rollback (nếu cần)

---

# 2. Objectives

Workflow phải đảm bảo:

- Chỉ release artifact đã được phê duyệt
- Build có thể tái lập (Reproducible Build)
- Có khả năng Rollback
- Có đầy đủ Audit Log
- Có Monitoring sau Release

---

# 3. Participants

| Agent | Responsibility |
|---------|---------------|
| Release Agent | Điều phối Release |
| Build Agent | Build Application |
| Package Agent | Đóng gói Artifact |
| Deploy Agent | Deploy |
| Validation Agent | Kiểm tra sau Deploy |
| Monitoring Agent | Theo dõi Production |
| Rollback Agent | Khôi phục phiên bản trước |

---

# 4. Trigger

Workflow được kích hoạt khi:

- Feature Workflow Completed
- Hotfix Workflow Completed
- Manual Approval
- Scheduled Release
- CI/CD Pipeline

---

# 5. Input

Workflow nhận các Artifact sau.

```
Source Artifact

↓

Review Report

↓

Test Report

↓

Version

↓

Release Configuration
```

---

# 6. Output

Workflow tạo:

```
Release Package

↓

Deployment Report

↓

Release Note

↓

Production Version
```

---

# 7. Release Types

Framework hỗ trợ nhiều loại Release.

| Type | Description |
|-------|-------------|
| Normal | Release thông thường |
| Patch | Sửa lỗi nhỏ |
| Hotfix | Khẩn cấp |
| Major | Phiên bản lớn |
| Rollback | Khôi phục |

---

# 8. High Level Flow

```
Approved Build

↓

Build

↓

Package

↓

Deploy

↓

Validate

↓

Monitor

↓

Completed
```

---

# 9. Step 1 - Pre-release Validation

Release Agent kiểm tra:

- Review Passed
- Test Passed
- Build Passed
- Security Scan Passed
- Version hợp lệ
- Branch đúng

Nếu bất kỳ điều kiện nào không đạt, Workflow dừng.

---

# 10. Step 2 - Build

Build Agent thực hiện:

```
Checkout Source

↓

Install Dependencies

↓

Compile

↓

Run Unit Test

↓

Generate Build
```

Output:

```
Build Artifact
```

---

# 11. Step 3 - Package

Package Agent tạo:

- Docker Image
- Zip Package
- Binary
- Helm Chart
- Static Assets

Output:

```
Release Package
```

---

# 12. Step 4 - Deploy

Deploy Agent triển khai theo chiến lược được cấu hình.

Ví dụ:

- Rolling Update
- Blue/Green
- Canary
- Feature Flag

Output:

```
Deployment Report
```

---

# 13. Step 5 - Post Deployment Validation

Validation Agent kiểm tra:

- Health Check
- API Check
- Smoke Test
- Database Connection
- External Services

Nếu thất bại

```
Rollback
```

---

# 14. Step 6 - Monitoring

Monitoring Agent theo dõi:

- Error Rate
- CPU
- Memory
- Latency
- Throughput
- User Sessions
- Crash Rate

Thời gian Monitoring có thể cấu hình.

---

# 15. Rollback

Rollback được kích hoạt khi:

- Health Check Failed
- Error Rate tăng bất thường
- Deployment Failed
- Smoke Test Failed

Flow

```
Current Version

↓

Restore Previous Version

↓

Verify

↓

Close Incident
```

---

# 16. Artifact Flow

```
Source Artifact

↓

Build Artifact

↓

Package Artifact

↓

Deployment Artifact

↓

Release Note

↓

Production
```

---

# 17. Sequence Diagram

```text
Approved Build
      │
      ▼
Release Agent
      │
      ▼
Build Agent
      │
      ▼
Package Agent
      │
      ▼
Deploy Agent
      │
      ▼
Validation Agent
      │
 ┌────┴────────────┐
 │ Validation OK ? │
 └────┬────────────┘
      │
 No   ▼
Rollback Agent
      │
      ▼
Production
      │
 Yes  ▼
Monitoring Agent
      │
      ▼
Completed
```

---

# 18. Quality Gates

| Gate | Condition |
|------|-----------|
| Build | Success |
| Review | Passed |
| Testing | Passed |
| Security | No Critical Issue |
| Validation | Success |
| Monitoring | Stable |

---

# 19. Release Strategies

Framework nên hỗ trợ:

### Rolling Update

Triển khai từng phần.

### Blue/Green

Hai môi trường song song.

### Canary

Triển khai cho một nhóm người dùng nhỏ.

### Feature Flag

Bật/tắt tính năng mà không cần Deploy lại.

---

# 20. Metrics

Workflow ghi nhận:

- Deployment Time
- Success Rate
- Rollback Count
- Downtime
- Build Duration
- Deployment Frequency
- MTTR
- AI Token Usage

---

# 21. Best Practices

✅ Không Release khi còn Critical Bug.

✅ Luôn có Rollback Plan.

✅ Theo dõi sau Release.

✅ Sinh Release Note tự động.

✅ Lưu toàn bộ Audit Log.

---

# 22. Anti-patterns

❌ Deploy trực tiếp từ máy cá nhân.

❌ Không kiểm tra Build.

❌ Không có Health Check.

❌ Không có Monitoring.

❌ Không có Rollback.

---

# 23. Example Workflow

```
Feature Workflow Completed

↓

Release Approval

↓

Build

↓

Package

↓

Deploy

↓

Smoke Test

↓

Monitoring

↓

Release Completed
```

---

# 24. Summary

Release Workflow là bước cuối cùng trong AI Software Factory.

Workflow đảm bảo rằng:

- Chỉ Artifact đã được xác thực mới được phát hành.
- Quá trình triển khai an toàn và có thể theo dõi.
- Có khả năng Rollback nhanh nếu phát hiện sự cố.
- Mọi hoạt động đều được ghi lại để phục vụ Audit và cải tiến quy trình.