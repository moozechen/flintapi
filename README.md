# 🔥 FlintAPI — One API Key. All Chinese LLMs.

<p align="center">
  <img src="https://flintapi.ai/favicon.svg" width="80" alt="FlintAPI" />
</p>

<p align="center">
  <strong>Access DeepSeek, Qwen, Kimi, GLM, MiniMax, and more through a single OpenAI-compatible endpoint.</strong><br>
  Self-hosted Qwen on PPU silicon. $2 free credit. No credit card.
</p>

<p align="center">
  <a href="https://flintapi.ai"><img src="https://img.shields.io/badge/website-flintapi.ai-purple" alt="Website"></a>
  <a href="https://flintapi.ai/docs"><img src="https://img.shields.io/badge/docs-API_Reference-blue" alt="Docs"></a>
  <a href="#models"><img src="https://img.shields.io/badge/models-25+-green" alt="Models"></a>
  <a href="https://github.com/tokenmall/flintapi/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-yellow" alt="License"></a>
</p>

---

## Why FlintAPI?

| | FlintAPI | Direct Provider | OpenRouter |
|---|---|---|---|
| **25+ Chinese LLMs** | ✅ One API key | ❌ Per-provider account | ✅ |
| **Self-hosted PPU Qwen** | ✅ Lower cost | ❌ Cloud pricing | ❌ |
| **OpenAI-compatible** | ✅ Drop-in replacement | ⚠️ Varies | ✅ |
| **Free credit** | ✅ $2, no card | ❌ | ⚠️ Limited |
| **No middleman markup** | ✅ Self-hosted | ✅ | ❌ Markup |
| **Referral bonus** | ✅ $1 each | ❌ | ❌ |

---

## Quick Start

### 1. Sign up (60 seconds)
```
https://flintapi.ai/register
```
Get your free $2 credit instantly. No credit card.

### 2. Get your API key
Find it in your [Dashboard](https://flintapi.ai/dashboard) → API Keys.

### 3. Make your first call

```bash
curl https://flintapi.ai/v1/chat/completions \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "deepseek-v4-pro",
    "messages": [{"role": "user", "content": "Explain quantum computing in one sentence."}]
  }'
```

### 4. Use any OpenAI SDK

```python
# pip install openai
from openai import OpenAI

client = OpenAI(
    base_url="https://flintapi.ai/v1",
    api_key="YOUR_API_KEY"
)

response = client.chat.completions.create(
    model="kimi-k2.6",
    messages=[{"role": "user", "content": "Hello!"}]
)
print(response.choices[0].message.content)
```

```javascript
// npm install openai
import OpenAI from 'openai';

const client = new OpenAI({
  baseURL: 'https://flintapi.ai/v1',
  apiKey: 'YOUR_API_KEY',
});

const completion = await client.chat.completions.create({
  model: 'qwen3.7-max',
  messages: [{ role: 'user', content: 'Say hello in Chinese' }],
});
console.log(completion.choices[0].message.content);
```

```go
// go get github.com/sashabaranov/go-openai
import "github.com/sashabaranov/go-openai"

client := openai.NewClient("YOUR_API_KEY")
client.BaseURL = "https://flintapi.ai/v1"

resp, _ := client.CreateChatCompletion(ctx, openai.ChatCompletionRequest{
    Model: "glm-5.1",
    Messages: []openai.ChatCompletionMessage{
        {Role: "user", Content: "Hello!"},
    },
})
```

---

## Models

| Model | Provider | Context | Best For |
|---|---|---|---|
| `deepseek-v4-pro` | DeepSeek | 128K | Reasoning, coding |
| `deepseek-v4-flash` | DeepSeek | 128K | Fast, cheap |
| `qwen3.7-max` | Qwen | 128K | Top quality |
| `qwen3.7-plus` | Qwen | 128K | Balanced |
| `qwen3.6-max-preview` | Qwen | 128K | Cutting edge |
| `qwen3.6-plus` | Qwen | 128K | General purpose |
| `qwen3.6-flash` | Qwen | 128K | Lowest latency |
| `qwen3.5-plus` | Qwen | 128K | All-rounder |
| `qwen3.5-flash` | Qwen | 128K | Fast & cheap |
| `qwen2.5-72b` | Qwen (PPU) | 32K | Self-hosted, cost-effective |
| `kimi-k2.6` | Kimi | 128K | Long context |
| `kimi-k2.5` | Kimi | 128K | Long context |
| `glm-5.1` | GLM | 128K | Bilingual expert |
| `glm-4.7` | GLM | 128K | Bilingual |
| `MiniMax/MiniMax-M2.7` | MiniMax | 128K | Creative writing |
| `MiniMax/MiniMax-M2.5` | MiniMax | 128K | Creative writing |
| `llama-3.3-70b` | Meta | 128K | Open source |
| `llama-3.1-8b` | Meta | 128K | Lightweight |
| `flint-smart` | FlintAPI | — | Auto-routing |

### Vision Models
| Model | Type |
|---|---|
| `qwen-image-2.0` | Text-to-image |
| `qwen-image-2.0-pro` | Pro image gen |
| `wan2.7-image` | Text-to-image |
| `wan2.7-image-pro` | Pro image gen |
| `xiaomi/mimo-v2.5` | Text-to-image |
| `xiaomi/mimo-v2.5-pro` | Pro image gen |

> 💡 Use `flint-smart` for automatic model routing — FlintAPI picks the best model for your request.

---

## 🚀 PPU Self-Hosted Inference

FlintAPI self-hosts **Qwen2.5-72B** on custom **PPU (Processing-in-Pixel Unit)** silicon.

- Lower cost than cloud GPU instances
- Competitive per-token pricing passed to you
- Same OpenAI-compatible API, lower bill

[Learn more about PPU →](https://flintapi.ai/docs)

---

## Streaming

```bash
curl https://flintapi.ai/v1/chat/completions \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "deepseek-v4-pro",
    "messages": [{"role": "user", "content": "Write a haiku about AI"}],
    "stream": true
  }'
```

---

## Referral Program

Refer a friend → **you both get $1 credit**.

1. Share your referral link: `https://flintapi.ai/register?ref=YOUR_CODE`
2. They sign up → you both earn $1
3. No limit on referrals

Find your referral code in [Dashboard](https://flintapi.ai/dashboard).

---

## Pricing

Pay-as-you-go. Per-token pricing varies by model. See live pricing at [flintapi.ai/pricing](https://flintapi.ai/pricing).

- **$2 free credit** — no credit card required
- **Top up** via Stripe (credit/debit card) or USDT (crypto)
- **No monthly fees, no hidden costs**

---

## API Reference

Base URL: `https://flintapi.ai/v1`

| Endpoint | Description |
|---|---|
| `GET /v1/models` | List all available models |
| `POST /v1/chat/completions` | Chat completion (OpenAI-compatible) |
| `GET /v1/models/{model_id}` | Get model details |

For detailed API docs, visit [flintapi.ai/docs](https://flintapi.ai/docs).

---

## Status

Check service status: [flintapi.ai](https://flintapi.ai)

---

## Community & Support

- 📧 Email: support@flintapi.ai
- 🐛 Issues: [GitHub Issues](https://github.com/tokenmall/flintapi/issues)
- 💬 Coming soon: Discord

---

## License

MIT © 2026 FlintAPI
