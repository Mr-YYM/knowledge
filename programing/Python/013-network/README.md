# Python 网络编程

处理流式数据

1. NDJSON流（每行一个JSON对象）



```python
import requests
import json

url = "http://localhost:11434/api/chat"
headers = {"Content-Type": "application/json"}
payload = {
    "model": "llama3.2",
    "messages": [{"role": "user", "content": "why is the sky blue?"}],
    "stream": True
}

try:
    with requests.post(url, json=payload, headers=headers, stream=True, timeout=30) as r:
        r.raise_for_status()  # 检查HTTP错误
        for line in r.iter_lines():
            if line:
                try:
                    data = json.loads(line)
                    print(data.get("message", "").get('content', ""), end="", flush=True)
                except json.JSONDecodeError as e:
                    print(f"\nJSON解析失败: {e}\n原始数据: {line}")
except requests.exceptions.RequestException as e:
    print(f"请求失败: {e}")
```

2. openai streaming: SSE


