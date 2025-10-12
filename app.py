# app.py（最小のLLMチャット。CloudでSecretsを使う前提）
import streamlit as st
from openai import OpenAI

st.title("🧪 Streamlit LLM App")

api_key = st.secrets.get("OPENAI_API_KEY")
if not api_key:
    st.error("OPENAI_API_KEY が未設定です（Manage app → Secrets に保存してください）")
    st.stop()

client = OpenAI(api_key=api_key)

prompt = st.text_input("質問をどうぞ")
if st.button("送信") and prompt:
    with st.spinner("LLMに問い合わせ中..."):
        resp = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.4,
        )
    st.write(resp.choices[0].message.content)

# 動作確認用（Secretsの有無だけ表示）
st.sidebar.write("Secrets:",
                 "✅ あり" if st.secrets.get("OPENAI_API_KEY") else "❌ なし")
