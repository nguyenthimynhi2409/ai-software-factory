# AI Software Factory

## Overview

AI Software Factory là framework sử dụng **Workflow + Agent +
Capability + Skill + Context Engineering** để tự động hóa vòng đời phát
triển phần mềm (AI-native SDLC).

Mục tiêu là để AI thực hiện phần lớn công việc của một nhóm phát triển
phần mềm:

-   Phân tích Requirement
-   Thiết kế
-   Sinh mã nguồn
-   Code Review
-   Tìm Bug
-   Sửa Bug
-   Sinh Test
-   Chạy Test
-   Release

Con người đóng vai trò Product Owner và phê duyệt kết quả.

------------------------------------------------------------------------

# Architecture

``` text
Workflow
    │
    ▼
Agent
    │
    ▼
Capability
    │
    ▼
Skill
    │
    ▼
Context Engineering
    │
    ▼
LLM Provider
    │
    ▼
Tools
```

## Core Concepts

### Workflow

Điều phối SDLC: - Feature - Bug Fix - Hotfix - Release

### Agent

Mỗi Agent đại diện một vai trò:

-   Requirement Agent
-   Planner Agent
-   Developer Agent
-   Reviewer Agent
-   Tester Agent
-   Bug Fix Agent
-   Release Agent

### Capability

Nhóm các Skill cùng lĩnh vực.

Ví dụ:

-   Development Capability
-   Review Capability
-   Testing Capability

### Skill

Skill chuẩn hóa cách AI thực hiện một nhiệm vụ.

Ví dụ:

-   Generate Component
-   Generate API
-   Generate Unit Test
-   Review Security
-   Fix Bug

### Context Engineering

Giảm timeout và hallucination bằng:

-   Hybrid Search
-   RAG
-   Lazy Loading
-   Hierarchical Summary
-   Context Compression
-   Memory

------------------------------------------------------------------------

# Project Structure

``` text
ai-software-factory/
├── apps/
├── packages/
│   ├── ai-core/
│   ├── ai-runtime/
│   ├── ai-agents/
│   ├── ai-capabilities/
│   ├── ai-skills/
│   ├── ai-workflows/
│   ├── ai-tools/
│   ├── ai-context/
│   ├── ai-memory/
│   ├── ai-artifacts/
│   ├── ai-prompts/
│   └── ai-llm/
└── docs/
```

# Feature Workflow

``` text
Requirement
    ↓
Requirement Agent
    ↓
Planner Agent
    ↓
Developer Agent
    ↓
Reviewer Agent
    ↓
Tester Agent
    ↓
Bug Fix Agent
    ↓
Retest
    ↓
Release Agent
```

# Prompt Pack

Prompt chuyên biệt cho project record thao tác người dùng, phân tích thành
test step, sinh code, review, tìm/sửa bug và re-test:

- [User Action Recording AI Workflow](docs/prompts/user-action-recording-ai-workflow.md)

# Prototype Source

Prototype chạy được cho pipeline record event thành test step nằm tại
`apps/action_pipeline/`. Chạy thử:

```bash
python -m unittest discover -s tests -v
python -m apps.action_pipeline examples/session.json
```

Các lớp chính:

- `models.py`: schema cho raw event, action và step.
- `normalizer.py`: sort, deduplicate, chuẩn hóa target và mask dữ liệu nhạy cảm.
- `analyzer.py`: chuyển action thành step có confidence và ambiguity.
- `pipeline.py`: orchestration boundary để sau này gắn LLM adapter.
- `cli.py`: giao diện chạy batch từ JSON.

# Guiding Principles

1.  Agent quyết định.
2.  Capability chọn Skill.
3.  Skill tạo Prompt.
4.  LLM sinh kết quả.
5.  Tool thực thi.
6.  Artifact là đầu ra giữa các Agent.
7.  Context chỉ nạp khi cần.

# Long-term Vision

AI Software Factory hướng đến một nền tảng có thể vận hành gần như toàn
bộ SDLC, trong đó con người tập trung vào chiến lược sản phẩm, còn AI
đảm nhận các công việc lặp lại, tiêu chuẩn hóa và có thể kiểm chứng.
