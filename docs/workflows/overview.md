# workflows/overview.md

# Workflow Engine

> "Workflow is the brain of AI Software Factory."

---

# 1. Overview

## What is Workflow?

Workflow là thành phần điều phối toàn bộ quá trình phát triển phần mềm.

Workflow **không sinh code**, **không review**, **không test**.

Workflow chỉ quyết định:

- Agent nào thực hiện tiếp theo.
- Agent nhận Artifact nào.
- Điều kiện để chuyển sang bước tiếp theo.
- Khi nào cần quay lại bước trước.

Workflow đóng vai trò tương tự:

- BPMN Workflow
- CI/CD Pipeline
- Business Process Engine
- State Machine

trong một hệ thống truyền thống.

---

# 2. Why Workflow?

Nếu chỉ sử dụng Prompt:

```
Requirement

↓

Claude

↓

Result
```

AI sẽ phải:

- đọc toàn bộ context
- tự quyết định mọi thứ
- khó mở rộng
- khó kiểm soát
- khó debug

AI Software Factory thay đổi cách tiếp cận.

```
Workflow

↓

Agent

↓

Capability

↓

Skill

↓

LLM
```

Workflow chịu trách nhiệm điều phối.

---

# 3. Responsibilities

Workflow chỉ có các trách nhiệm sau.

## Decide Next Step

Ví dụ

```
Requirement Completed

↓

Developer Agent
```

---

## Pass Artifact

Ví dụ

```
Developer Agent

↓

Source Code Artifact

↓

Review Agent
```

---

## Retry

Ví dụ

```
Testing Failed

↓

Bug Fix Agent
```

---

## Stop Workflow

Ví dụ

```
Requirement Invalid

↓

Workflow End
```

---

## Record State

Ví dụ

```
Feature

Planning

Completed
```

---

# 4. Workflow Lifecycle

```
Created

↓

Running

↓

Waiting

↓

Completed

↓

Archived
```

Nếu xảy ra lỗi

```
Running

↓

Failed

↓

Retry

↓

Running
```

---

# 5. Workflow Components

Một Workflow gồm các thành phần sau.

```
Workflow

├── Metadata

├── States

├── Transitions

├── Conditions

├── Events

├── Agents

├── Artifacts

└── Policies
```

---

## Metadata

Ví dụ

```yaml
name: Feature Development

version: 1.0

owner: Product Team

description: Create a new feature
```

---

## States

Ví dụ

```
Planning

↓

Development

↓

Review

↓

Testing

↓

Release
```

---

## Transition

Ví dụ

```
Review Passed

↓

Testing
```

Nếu fail

```
Review Failed

↓

Development
```

---

## Events

Ví dụ

```
RequirementCreated

TaskGenerated

CodeGenerated

ReviewCompleted

TestingCompleted

Released
```

---

## Artifacts

Workflow không truyền text.

Workflow truyền Artifact.

Ví dụ

```
Requirement Artifact

↓

Developer Agent
```

Developer tạo

```
Source Artifact
```

Review sử dụng

```
Source Artifact
```

---

# 6. Standard Workflow

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

Bug Fix

↓

Retest

↓

Release
```

---

# 7. Workflow Types

AI Software Factory hỗ trợ nhiều Workflow.

```
Feature Development

Bug Fix

Hotfix

Release

Research

Spike

Refactor

Code Review

Testing
```

Mỗi Workflow là độc lập.

---

# 8. Event Driven Workflow

Workflow hoạt động theo Event.

Ví dụ

```
Requirement Created

↓

Planner Agent

↓

Task Created

↓

Developer Agent

↓

Code Generated

↓

Review Agent
```

Không Agent nào gọi trực tiếp Agent khác.

Workflow là nơi điều phối.

---

# 9. Workflow State Machine

```
┌─────────────┐
│ Requirement │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Planning    │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Development │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Review      │
└──────┬──────┘
       │
  Pass │ Fail
       │
       ▼
┌─────────────┐
│ Testing     │
└──────┬──────┘
       │
  Fail │ Pass
       ▼
┌─────────────┐
│ Bug Fix     │
└──────┬──────┘
       │
       ▼
   Testing
```

---

# 10. Workflow Template

Mỗi Workflow nên tuân theo cấu trúc sau.

```yaml
name:

description:

trigger:

agents:

artifacts:

states:

transitions:

completion_condition:

rollback_policy:
```

---

# 11. Design Principles

## Principle 1

Workflow không chứa Prompt.

---

## Principle 2

Workflow không chứa Business Logic.

---

## Principle 3

Workflow chỉ điều phối.

---

## Principle 4

Workflow chỉ truyền Artifact.

---

## Principle 5

Workflow không phụ thuộc LLM.

---

# 12. Best Practices

✅ Workflow nhỏ.

✅ Một Workflow chỉ có một mục tiêu.

✅ Event Driven.

✅ Stateless.

✅ Retry được.

✅ Có Rollback.

---

# 13. Anti-patterns

❌ Workflow tự generate code.

❌ Workflow gọi trực tiếp Claude.

❌ Workflow đọc Repository.

❌ Workflow xử lý Prompt.

❌ Workflow thao tác Git.

---

# 14. Example

Feature Development

```
Requirement

↓

Requirement Agent

↓

Planner Agent

↓

Developer Agent

↓

Review Agent

↓

Testing Agent

↓

Bug Fix Agent

↓

Release Agent
```

---

# 15. Summary

Workflow là tầng cao nhất của AI Software Factory.

Workflow không biết:

- Prompt
- Claude
- GPT
- Code

Workflow chỉ biết:

- Agent
- Artifact
- Event
- State

Đây là nguyên tắc quan trọng nhất giúp AI Software Factory có thể mở rộng và thay thế từng thành phần mà không ảnh hưởng toàn bộ hệ thống.
