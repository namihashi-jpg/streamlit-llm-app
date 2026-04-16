import streamlit as st

st.set_page_config(page_title="企業向けサイバー対応セルフチェック", layout="wide")

st.title("企業向けサイバー対応セルフチェック")
st.write("担当者が事前に入力し、自社の対応状況を確認するための簡易診断アプリです。")

st.header("基本情報")
company_name = st.text_input("会社名")
industry = st.selectbox(
    "業種",
    ["製造業", "流通業", "小売業", "サービス業", "IT・情報通信業", "医療・福祉", "その他"]
)
company_size = st.selectbox(
    "企業規模",
    ["1〜49名", "50〜299名", "300〜999名", "1000名以上"]
)
role = st.selectbox(
    "入力者の立場",
    ["情報システム担当", "総務", "セキュリティ担当", "管理部門", "経営企画", "その他"]
)

st.header("診断項目")
st.write("各項目について、現在の状況に最も近いものを選んでください。")

options = ["対応済み", "一部対応", "未対応"]

st.subheader("指示1：方針（リスク認識）")
q1 = st.radio("1. 経営層に対して、サイバーセキュリティリスクを定期的に報告していますか？", options, key="q1")
q2 = st.radio("2. 他社のサイバー攻撃事例や被害を、自社への影響とセットで説明していますか？", options, key="q2")
q3 = st.radio("3. セキュリティポリシーに『サイバー攻撃による業務停止』などの観点が含まれていますか？", options, key="q3")

st.subheader("指示2：体制（組織）")
q4 = st.radio("4. サイバーセキュリティの責任者（CISOなど）が明確ですか？", options, key="q4")
q5 = st.radio("5. インシデント発生時の役割分担（誰が何をするか）が決まっていますか？", options, key="q5")
q6 = st.radio("6. IT部門以外（総務・法務・事業部門）も関与した体制になっていますか？", options, key="q6")

st.subheader("指示3：資源（予算・人材）")
q7 = st.radio("7. セキュリティ対策のための予算が確保されていますか？", options, key="q7")
q8 = st.radio("8. 必要なセキュリティ人材・スキルが定義されていますか？", options, key="q8")
q9 = st.radio("9. 外部ベンダーや専門家の活用方針がありますか？", options, key="q9")

st.subheader("指示4：生成AI利用とサイバーセキュリティ対応")
q10 = st.radio("10. 生成AIの利用に関する社内ルール（入力してよい情報・禁止情報）を整備していますか？", options, key="q10")
q11 = st.radio("11. 生成AI利用に伴うリスク（誤情報、個人情報、機密情報、知財、攻撃悪用）を整理していますか？", options, key="q11")
q12 = st.radio("12. 生成AIをセキュリティ対策（情報収集、分析、検知支援）に活用する検討をしていますか？", options, key="q12")
if st.button("診断する"):
    score_map = {
        "対応済み": 2,
        "一部対応": 1,
        "未対応": 0
    }

    scores = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12]
    total_score = sum(score_map[q] for q in scores)

    score_1 = sum(score_map[q] for q in [q1, q2, q3])
    score_2 = sum(score_map[q] for q in [q4, q5, q6])
    score_3 = sum(score_map[q] for q in [q7, q8, q9])
    score_4 = sum(score_map[q] for q in [q10, q11, q12])

    def evaluate(score):
        if score <= 2:
            return "要対応（高）"
        elif score <= 4:
            return "改善余地あり（中）"
        else:
            return "良好（低）"

    st.header("診断結果")

    st.write(f"**会社名**: {company_name if company_name else '未入力'}")
    st.write(f"**業種**: {industry}")
    st.write(f"**企業規模**: {company_size}")
    st.write(f"**入力者**: {role}")

    st.subheader("総合評価")
    if total_score <= 6:
        st.error("総合評価：要対応（優先度 高）")
    elif total_score <= 12:
        st.warning("総合評価：改善余地あり（優先度 中）")
    else:
        st.success("総合評価：良好（優先度 低）")

    st.subheader("項目別評価")
    st.write(f"**指示1：方針（リスク認識）** → {evaluate(score_1)}")
    st.write(f"**指示2：体制（組織）** → {evaluate(score_2)}")
    st.write(f"**指示3：資源（予算・人材）** → {evaluate(score_3)}")
    st.write(f"**指示4：生成AI利用とサイバーセキュリティ対応** → {evaluate(score_4)}")

    st.subheader("次の一手（提案）")

    if score_1 <= 2:
        st.write("**指示1への提案**")
        st.write("- 経営会議で月1回のサイバーリスク報告を始める")
        st.write("- 他社被害事例を使って、自社への影響を説明する")
        st.write("- セキュリティポリシーにサイバー攻撃・業務停止の観点を追加する")

    if score_2 <= 2:
        st.write("**指示2への提案**")
        st.write("- サイバーセキュリティ責任者を明確にする")
        st.write("- インシデント発生時の役割分担を文書化する")
        st.write("- IT部門だけでなく総務・法務・事業部門も含めた体制を作る")

    if score_3 <= 2:
        st.write("**指示3への提案**")
        st.write("- セキュリティ対策専用の予算項目を設ける")
        st.write("- 必要なスキル・人材像を明確にする")
        st.write("- 外部ベンダーや専門家の活用方針を決める")

    if score_4 <= 2:
        st.write("**指示4への提案**")
        st.write("- 生成AIの利用ルールを整備する")
        st.write("- 機密情報・個人情報・知的財産の入力可否を明文化する")
        st.write("- 生成AI利用に伴うリスク（誤情報、攻撃悪用など）を整理する")
        st.write("- 情報収集や分析など、セキュリティ業務でのAI活用対象を洗い出す")
        
    if score_1 > 2 and score_2 > 2 and score_3 > 2:
        st.write("全体として一定の対応が進んでいます。次はPDCAやインシデント対応体制の深掘りを検討してください。")
#a
