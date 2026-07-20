# 🔥 FlintAPI — AI Consulting Engine + Smart Routing

<p align="center">
  <img src="https://flintapi.ai/favicon.svg" width="80" alt="FlintAPI logo" />
</p>

<p align="center">
  <a href="https://flintapi.ai"><img src="https://img.shields.io/badge/status-online-brightgreen" alt="Status"></a>
  <a href="https://pypi.org/project/flintapi/"><img src="https://img.shields.io/badge/python-3.8%2B-blue" alt="Python"></a>
  <a href="https://github.com/moozechen/flintapi/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-green" alt="License"></a>
  <a href="https://flintapi.ai/docs"><img src="https://img.shields.io/badge/docs-flintapi.ai-purple" alt="Docs"></a>
</p>

<p align="center">
  <b>AI Consulting Engine that decomposes complex questions,<br/>routes each sub-task to the optimal model, and synthesizes expert output.<br/><a href="https://flintapi.ai/register">$5 free credit — no card required.</a></b>
</p>

---

## 🧠 flint-consulting: AI-Powered Expert Analysis

FlintAPI's **consulting engine** (`flint-consulting`) uses multi-model synthesis to produce McKinsey-style strategic reports. It decomposes complex business and technical questions, dispatches sub-tasks to specialized models, and synthesizes the results into comprehensive, structured analyses.

### Example: Cloud Platform Comparison

```bash
curl https://flintapi.ai/v1/chat/completions \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "flint-consulting",
    "messages": [{"role": "user", "content": "Compare AWS vs GCP for an AI-native startup with 20 engineers"}]
  }'
```

**Sample output** (from real consulting report, July 2026):

> *"GCP's integrated AI stack (Vertex AI + Gemini ecosystem) offers 30-40% faster time-to-first-prototype than AWS. GCP deployments reached production 22% faster (median 18 days vs. 23 days). Total 2-year TCO for AI/ML workloads: $96,900 (GCP) vs. $123,000 (AWS) — a 21% savings."*

### Example: Protocol Architecture Decision

```bash
curl https://flintapi.ai/v1/chat/completions \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{"model":"flint-consulting","messages":[{"role":"user","content":"WebSocket vs SSE vs gRPC for a real-time dashboard with 10K concurrent users"}]}'
```

**Sample output** (from real consulting report, July 2026):

> *"68% of teams over-engineer their real-time layer. For server-push-only workloads like dashboards, SSE delivers identical performance with zero operational overhead. Benchmark: SSE at 12% CPU / 480MB / 45ms P99 for 10K concurrent — statistically indistinguishable from WebSocket at 14% CPU / 520MB / 42ms P99."*

### How flint-consulting Works

| Stage | Model(s) | Function |
|-------|----------|----------|
| **Decompose** | `deepseek-v4-flash` | MECE breakdown of the question into independent sub-tasks |
| **Analyze (parallel)** | `deepseek-v4-pro`, `qwen3.7-max`, `glm-5.1` | Each sub-task assigned to the best specialist model |
| **Synthesize** | `deepseek-v4-pro` | Weave results into one coherent report with confidence scoring |
| **Verify** | `qwen3.7-max` | Cross-reference facts, flag contradictions, assign confidence (0-1) |

**Published consulting reports**: [AWS vs GCP (cloud strategy)](https://flintapi.ai/blog?post=aws-vs-gcp-consulting) · [WebSocket vs SSE vs gRPC (protocols)](https://flintapi.ai/blog?post=websocket-sse-grpc-consulting) · [Full blog →](https://flintapi.ai/blog)

---

## Why FlintAPI?

FlintAPI is an **AI Consulting Engine** powered by Smart Routing. When you send a prompt, FlintAPI's router **decomposes** it into sub-tasks, **dispatches** each to the best-suited model, and returns the combined result. You never need to pick a model.

| | FlintAPI | Direct Provider | OpenRouter |
|---|:---:|:---:|:---:|
| **AI Consulting** | ✅ Multi-model synthesis | ❌ Single-model | ❌ Basic routing only |
| **Smart Routing** | ✅ Decompose & Dispatch | ❌ Manual model selection | ❌ Basic routing only |
| **OpenAI-compatible** | ✅ Drop-in replacement | ⚠️ Varies | ✅ |
| **Free credit** | ✅ $5, no card | ❌ | ⚠️ Limited |
| **Referral bonus** | ✅ $1 each | ❌ | ❌ |
| **Multi-SDK** | ✅ Python, Node, Go, curl | ⚠️ Per-provider | ✅ |

---

## Quick Start (60 seconds)

### 1. Register
Go to [flintapi.ai/register](https://flintapi.ai/register) — you get **$5 free credit** instantly, no credit card required.

### 2. Get your API Key
Find it in your [Dashboard](https://flintapi.ai/dashboard) → Settings → Create Key. Copy it — it's shown only once!

### 3. Make your first call

**cURL:**
```bash
curl https://flintapi.ai/v1/chat/completions \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "flint-consulting",
    "messages": [{"role": "user", "content": "Should my startup use AWS or GCP?"}]
  }'
```

**Python** (with `pip install openai`):
```python
from openai import OpenAI

client = OpenAI(
    base_url="https://flintapi.ai/v1",
    api_key="YOUR_API_KEY"
)

response = client.chat.completions.create(
    model="flint-consulting",
    messages=[{"role": "user", "content": "Compare WebSocket vs SSE vs gRPC"}]
)
print(response.choices[0].message.content)
```

**Node.js** (`npm install openai`):
```javascript
import OpenAI from 'openai';

const client = new OpenAI({
  baseURL: 'https://flintapi.ai/v1',
  apiKey: 'YOUR_API_KEY',
});

const completion = await client.chat.completions.create({
  model: 'flint-consulting',
  messages: [{ role: 'user', content: 'Compare cloud providers for AI workloads' }],
});
console.log(completion.choices[0].message.content);
```

**Go** (`go get github.com/sashabaranov/go-openai`):
```go
import "github.com/sashabaranov/go-openai"

client := openai.NewClient("YOUR_API_KEY")
client.BaseURL = "https://flintapi.ai/v1"

resp, _ := client.CreateChatCompletion(ctx, openai.ChatCompletionRequest{
    Model: "flint-consulting",
    Messages: []openai.ChatCompletionMessage{
        {Role: "user", Content: "AWS vs GCP for AI startup?"},
    },
})
fmt.Println(resp.Choices[0].Message.Content)
```

---

## 🧠 flint-smart Router

Use `"model": "flint-smart"` for general-purpose auto-routing. Use `"model": "flint-consulting"` for multi-model synthesized reports.

| Model | Best For |
|-------|----------|
| `flint-consulting` | Strategic reports, comparisons, architecture decisions, technical analysis |
| `flint-smart` | General chat, coding, quick Q&A with auto model selection |

| Prompt Type | flint-smart Routes To | Why |
|-------------|-----------|-----|
| Code / programming | `deepseek-v4-pro` | #1 coding benchmark (Aider) |
| Creative writing | `MiniMax-M2.7` | Fluency & style, 512K context |
| Chinese / bilingual | `glm-5.1` | Bilingual expert, enterprise-grade |
| Reasoning / analysis | `qwen3.7-max` | Flagship all-rounder, strong logic |
| General / default | `deepseek-v4-flash` | Fast, cost-effective fallback |

---

## 📊 Available Models

The Smart Router automatically selects from these models:

| Model | Provider | Context | Best For |
|-------|----------|---------|----------|
| `deepseek-v4-pro` | DeepSeek | 128K | Reasoning & code |
| `deepseek-v4-flash` | DeepSeek | 128K | Fast, cost-effective |
| `qwen3.7-max` | Qwen | 128K | Flagship all-rounder |
| `qwen3.7-plus` | Qwen | 128K | Balanced Chinese-English |
| `qwen3.5-plus` | Qwen | 128K | Solid general-purpose |
| `qwen3.5-flash` | Qwen | 128K | Lowest latency |
| `kimi-k2.6` | Kimi | 256K | Long context |
| `kimi-k2.5` | Kimi | 128K | Long context |
| `glm-5.1` | GLM | 32K | Bilingual expert |
| `MiniMax-M2.7` | MiniMax | 512K | Creative writing |

Full list & pricing: [flintapi.ai/pricing](https://flintapi.ai/pricing)

---

## 🔌 Python SDK

A thin OpenAI-compatible wrapper lives in [`flintapi/`](./flintapi) in this repo. Install it directly from source:

```bash
pip install git+https://github.com/moozechen/flintapi.git
```

```python
from flintapi import Flint

flint = Flint(api_key="YOUR_API_KEY")

# Consulting report
report = flint.chat("Compare AWS vs GCP for AI startups", model="flint-consulting")
print(report)

# Smart routing
reply = flint.chat("Write a Python quicksort", model="flint-smart")
print(reply)

# Streaming
for chunk in flint.chat_stream("Tell me a story"):
    print(chunk, end="")
```

---

## 📖 Docs & Resources

- [API Docs](https://flintapi.ai/docs) — Full API reference with code examples
- [Playground](https://flintapi.ai/playground) — Try models in your browser
- [Pricing](https://flintapi.ai/pricing) — Per-token pricing for all models
- [Compare](https://flintapi.ai/compare) — FlintAPI vs alternatives
- [Blog](https://flintapi.ai/blog) — Consulting reports, guides, and tutorials
- [Status](https://flintapi.ai/status) — Real-time model health
- [Dashboard](https://flintapi.ai/dashboard) — Usage, billing, API keys

---

## 🌟 Features

- **AI Consulting Engine** — Multi-model synthesis for strategic analysis and technical reports
- **Smart Routing** — Decompose & Dispatch: one prompt auto-routed to optimal models per sub-task
- **OpenAI-compatible** — change `base_url` and keep existing code
- **flint-smart router** — auto-select best model per request  
- **$5 free credit** — instant, no card required
- **Real-time billing** — per-token pricing, usage dashboard
- **4 language SDKs** — cURL, Python, Node.js, Go
- **Referral program** — both you and your friend get $1

---

## 🚀 Architecture

FlintAPI runs as a hosted service on [flintapi.ai](https://flintapi.ai) — just grab a key and call the `/v1` endpoints. This repo ships the open-source **Python SDK**; the routing engine itself is operated as a managed service.

To use the SDK from source:

```bash
git clone https://github.com/moozechen/flintapi.git
cd flintapi
pip install -e .
```

**Production stack:**
- **Frontend:** React 18 + Vite, served via Nginx
- **Backend:** FastAPI (Python 3.10+), OpenAI-compatible `/v1` endpoints
- **Consulting Engine:** flint-consulting — multi-model MECE decomposition + parallel execution + synthesis
- **Router:** flint-smart decompose & dispatch engine
- **Database:** SQLite (token relay, usage logs)
- **Deployment:** Ubuntu 22.04, Nginx reverse proxy, Let's Encrypt SSL

---

## 🤝 Support

- Email: [support@flintapi.ai](mailto:support@flintapi.ai)
- GitHub Issues: [github.com/moozechen/flintapi/issues](https://github.com/moozechen/flintapi/issues)
- Website: [flintapi.ai](https://flintapi.ai)

---

## 🇨🇳 Chinese AI Landscape (2026)

> A community resource tracking the Chinese LLM ecosystem. Not promotional — just what's out there, what each model does best, and how to try them.

### The Major Players

| Model | Organization | Open Weights | Best For | How to Try |
|-------|-------------|:---:|----------|------------|
| **DeepSeek-V4-Pro** | DeepSeek | ✅ | Reasoning, math, code | [api-docs.deepseek.com](https://api-docs.deepseek.com) |
| **Qwen3.7-Max** | Alibaba | ✅ | All-rounder, bilingual | [qwen.ai](https://qwen.ai) |
| **Kimi-K2.6** | Moonshot AI | ❌ API only | Long context (256K) | [kimi.moonshot.cn](https://kimi.moonshot.cn) |
| **GLM-5.1** | Zhipu AI | ✅ | Bilingual enterprise | [zhipuai.cn](https://zhipuai.cn) |
| **MiniMax-M2.7** | MiniMax | ❌ API only | Creative writing, 512K ctx | [minimaxi.com](https://minimaxi.com) |
| **Doubao-1.5-pro** | ByteDance | ❌ API only | Chinese content, fast | [volcengine.com](https://www.volcengine.com) |
| **Baichuan-M1** | Baichuan | ✅ | Healthcare, finance | [baichuan-ai.com](https://www.baichuan-ai.com) |
| **Yi-Lightning** | 01.AI | ✅ | Efficient, low-latency | [01.ai](https://01.ai) |

### Why They Matter

- **DeepSeek-V4** scored #1 on [Aider's polyglot coding benchmark](https://aider.chat/docs/leaderboards/), beating GPT-5 and Claude
- **Qwen3.6-35B-A3B** (MoE) delivers near-70B performance at 35B params — [1274 points on HN](https://news.ycombinator.com/item?id=47792764)
- **Qwen3.6-27B** runs on a single RTX 3090 (Q4 quant) at 50-70 tok/s — [HN front page](https://news.ycombinator.com/item?id=48721903)
- **Kimi-K2.6** handles 256K context windows, competitive with Gemini for long-document tasks
- **MiniMax-M2.7** has 512K context — among the longest available worldwide

### Community Benchmarks

| Benchmark | Top Chinese Model | Score vs GPT-5 |
|-----------|------------------|:---:|
| [Aider Polyglot](https://aider.chat/docs/leaderboards/) (coding) | DeepSeek-V4-Pro | +5.2% |
| [LiveCodeBench](https://livecodebench.github.io/) | Qwen3.7-Max | -2.1% |
| MMLU-Pro | DeepSeek-V4-Pro | -1.8% |
| C-Eval (Chinese NLP) | Qwen3.7-Max | +8.3% |

*Benchmarks from official model cards and public leaderboards. Last updated: June 2026.*

### Getting Started

1. **Via API**: Most providers offer OpenAI-compatible endpoints — sign up, get a key, swap `base_url`
2. **Run locally**: Qwen3.6-27B fits on a 3090; DeepSeek-V4 needs ~140GB VRAM (run on cloud or multiple GPUs)
3. **Registration tip**: Some platforms require Chinese phone numbers — use Alibaba Cloud's [international portal](https://www.alibabacloud.com/en/product/tongyi-qwen) for Qwen without Chinese ID

---

*Community-maintained resource. Spotted outdated info? [Open an issue](https://github.com/moozechen/flintapi/issues).*