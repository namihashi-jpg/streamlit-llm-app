import streamlit as st
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO

st.set_page_config(page_title="企業向けサイバー対応セルフチェック", layout="wide")

st.title("企業向けサイバー対応セルフチェック")
st.write("担当者が事前に入力し、自社の対応状況やSCS評価制度における現時点の到達見込みを確認するための自己診断アプリです。")
st.info("本結果は自己診断に基づく参考値です。正式な認証・評価を示すものではありません。")

# ----------------------------
# 基本情報
# ----------------------------
st.header("基本情報")

company_name = st.text_input("会社名")
industry = st.selectbox(
    "業種",
    ["製造業", "建設業", "流通業", "小売業", "サービス業", "IT・情報通信業", "医療・福祉", "金融業", "その他"]
)
company_size = st.selectbox(
    "企業規模",
    ["1〜49名", "50〜299名", "300〜999名", "1000名以上"]
)
role = st.selectbox(
    "入力者の立場",
    ["情報システム担当", "総務", "セキュリティ担当", "管理部門", "経営企画", "その他"]
)

options = ["対応済み", "一部対応", "未対応"]

st.header("診断項目")
st.write("各項目について、現在の状況に最も近いものを選んでください。")

# ----------------------------
# 1. ガバナンスの整備
# ----------------------------
st.subheader("1. ガバナンスの整備")

q1 = st.radio("1. セキュリティに関する法令等を考慮した社内ルールを策定し、周知していますか", options, key="q1")
q2 = st.radio("2. セキュリティ推進活動を担当する部署・役員・従業員を決定し、責任と権限を割り当てていますか", options, key="q2")
q3 = st.radio("3. サイバー攻撃やその予兆を監視・分析する体制がありますか", options, key="q3")
q4 = st.radio("4. 守秘義務のルールを策定し、遵守させていますか", options, key="q4")
q5 = st.radio("5. 自社のセキュリティ対応方針を策定し、周知していますか", options, key="q5")
q6 = st.radio("6. セキュリティ対策推進計画を策定し、経営層へ定期報告して改善に反映していますか", options, key="q6")

# ----------------------------
# 2. 取引先管理
# ----------------------------
st.subheader("2. 取引先管理")

q7 = st.radio("7. 取引先と自社とのビジネス上またはシステム上の関係を把握していますか", options, key="q7")
q8 = st.radio("8. 自社の機密情報の取扱方法を共有先との間で明確にしていますか", options, key="q8")
q9 = st.radio("9. 自社に影響を及ぼす可能性のある取引先のセキュリティ対策状況を把握していますか", options, key="q9")
q10 = st.radio("10. セキュリティインシデント発生時の、他社との役割・責任を明確にしていますか", options, key="q10")
q11 = st.radio("11. 契約終了時に、自社の機密情報やアクセス権を回収・破棄するルールがありますか", options, key="q11")

# ----------------------------
# 3. リスクの特定
# ----------------------------
st.subheader("3. リスクの特定")

q12 = st.radio("12. 情報機器、OS、ソフトウェアに関する情報を把握していますか", options, key="q12")
q13 = st.radio("13. ネットワークに関する情報を把握する仕組みがありますか", options, key="q13")
q14 = st.radio("14. 重要な情報資産を特定していますか", options, key="q14")
q15 = st.radio("15. 情報資産ごとの管理責任者を定めていますか", options, key="q15")
q16 = st.radio("16. 情報資産に対する脅威・脆弱性・影響を把握していますか", options, key="q16")
q17 = st.radio("17. サイバーセキュリティリスクを評価する手順がありますか", options, key="q17")
q18 = st.radio("18. リスク評価結果をもとに対応優先順位を決めていますか", options, key="q18")

# ----------------------------
# 4. 対策の実装
# ----------------------------
st.subheader("4. 対策の実装")

q19 = st.radio("19. 利用者ごとのアクセス権限を適切に設定していますか", options, key="q19")
q20 = st.radio("20. アカウントの作成・変更・削除ルールがありますか", options, key="q20")
q21 = st.radio("21. 退職者・異動者のアカウントを速やかに無効化していますか", options, key="q21")
q22 = st.radio("22. 多要素認証を必要に応じて導入していますか", options, key="q22")
q23 = st.radio("23. OSやソフトウェアの脆弱性情報を収集していますか", options, key="q23")
q24 = st.radio("24. セキュリティパッチを適時適切に適用していますか", options, key="q24")
q25 = st.radio("25. 端末やサーバにマルウェア対策を実施していますか", options, key="q25")
q26 = st.radio("26. メールやファイルを介した感染を防ぐ対策がありますか", options, key="q26")
q27 = st.radio("27. 通信の制御・分離などのネットワーク防御策がありますか", options, key="q27")
q28 = st.radio("28. 外部公開システムへの防御対策がありますか", options, key="q28")
q29 = st.radio("29. 不正通信や異常通信を検知する仕組みがありますか", options, key="q29")
q30 = st.radio("30. 重要データのバックアップを取得していますか", options, key="q30")
q31 = st.radio("31. バックアップから復旧できることを確認していますか", options, key="q31")

# ----------------------------
# 5. 検知・監視
# ----------------------------
st.subheader("5. 検知・監視")

q32 = st.radio("32. アクセスログや操作ログを取得していますか", options, key="q32")
q33 = st.radio("33. ログを一定期間保管していますか", options, key="q33")
q34 = st.radio("34. ログを定期的に確認・分析していますか", options, key="q34")
q35 = st.radio("35. サイバー攻撃や不審な挙動を監視する仕組みがありますか", options, key="q35")
q36 = st.radio("36. 監視結果をもとに初動対応につなげる体制がありますか", options, key="q36")

# ----------------------------
# 6. インシデント対応
# ----------------------------
st.subheader("6. インシデント対応")

q37 = st.radio("37. インシデント発生時の対応手順書がありますか", options, key="q37")
q38 = st.radio("38. 連絡先一覧を整備し、すぐ連絡できる状態ですか", options, key="q38")
q39 = st.radio("39. 重大度に応じた判断・エスカレーションルールがありますか", options, key="q39")
q40 = st.radio("40. 事業継続や復旧のための計画がありますか", options, key="q40")
q41 = st.radio("41. 事業停止を想定した訓練・演習を行っていますか", options, key="q41")
q42 = st.radio("42. 顧客・取引先・関係機関への報告や公表ルールがありますか", options, key="q42")
q43 = st.radio("43. インシデント後に再発防止を実施し、見直す仕組みがありますか", options, key="q43")

# ----------------------------
# 7. 生成AI拡張チェック
# ----------------------------
st.subheader("7. 生成AI拡張チェック")

q44 = st.radio("44. 生成AIの利用に関する社内ルールを整備していますか", options, key="q44")
q45 = st.radio("45. 生成AI利用に伴うリスク（誤情報、個人情報、機密情報、知財、攻撃悪用）を整理していますか", options, key="q45")
q46 = st.radio("46. 生成AIをセキュリティ対策（情報収集、分析、検知支援）に活用する検討をしていますか", options, key="q46")

if st.button("診断する"):
    score_map = {
        "対応済み": 2,
        "一部対応": 1,
        "未対応": 0
    }

    answers = {
        "q1": q1, "q2": q2, "q3": q3, "q4": q4, "q5": q5,
        "q6": q6, "q7": q7, "q8": q8, "q9": q9, "q10": q10,
        "q11": q11, "q12": q12, "q13": q13, "q14": q14,
        "q15": q15, "q16": q16, "q17": q17, "q18": q18,
        "q19": q19, "q20": q20, "q21": q21, "q22": q22,
        "q23": q23, "q24": q24, "q25": q25, "q26": q26,
        "q27": q27, "q28": q28, "q29": q29, "q30": q30,
        "q31": q31, "q32": q32, "q33": q33, "q34": q34,
        "q35": q35, "q36": q36, "q37": q37, "q38": q38,
        "q39": q39, "q40": q40, "q41": q41, "q42": q42,
        "q43": q43, "q44": q44, "q45": q45, "q46": q46
    }

    total_score = sum(score_map[a] for a in answers.values())
    max_score = len(answers) * 2
    score_ratio = round((total_score / max_score) * 100, 1)

    score_1 = sum(score_map[answers[f"q{i}"]] for i in range(1, 7))
    score_2 = sum(score_map[answers[f"q{i}"]] for i in range(7, 12))
    score_3 = sum(score_map[answers[f"q{i}"]] for i in range(12, 19))
    score_4 = sum(score_map[answers[f"q{i}"]] for i in range(19, 32))
    score_5 = sum(score_map[answers[f"q{i}"]] for i in range(32, 37))
    score_6 = sum(score_map[answers[f"q{i}"]] for i in range(37, 44))
    score_7 = sum(score_map[answers[f"q{i}"]] for i in range(44, 47))

    scs_star3_questions = [f"q{i}" for i in range(1, 27)]
    scs_star4_questions = [f"q{i}" for i in range(1, 44)]

    star3_scores = [score_map[answers[q]] for q in scs_star3_questions]
    star4_scores = [score_map[answers[q]] for q in scs_star4_questions]

    star3_unmet = sum(1 for s in star3_scores if s == 0)
    star3_partial = sum(1 for s in star3_scores if s == 1)
    star4_unmet = sum(1 for s in star4_scores if s == 0)
    star4_partial = sum(1 for s in star4_scores if s == 1)

    if star3_unmet == 0 and star3_partial <= 5:
        if star4_unmet == 0 and star4_partial <= 8:
            star_result = "★4相当（自己判定）"
        else:
            star_result = "★3相当（自己判定）"
    else:
        star_result = "未達（★3水準に未到達）"

    def evaluate(score, max_score_part):
        ratio = score / max_score_part
        if ratio < 0.5:
            return "要対応（高）"
        elif ratio < 0.8:
            return "改善余地あり（中）"
        else:
            return "良好（低）"

    st.header("診断結果")

    st.write(f"**会社名**: {company_name if company_name else '未入力'}")
    st.write(f"**業種**: {industry}")
    st.write(f"**企業規模**: {company_size}")
    st.write(f"**入力者**: {role}")

    st.subheader("総合スコア")
    st.write(f"**総合スコア**: {total_score} / {max_score}")
    st.write(f"**達成率**: {score_ratio}%")
    st.progress(total_score / max_score)

    st.subheader("SCS自己判定")
    if "★4" in star_result:
        st.success(star_result)
    elif "★3" in star_result:
        st.warning(star_result)
    else:
        st.error(star_result)

    st.caption("本結果は自己診断に基づく参考値です。正式な認証・評価を示すものではありません。")

    st.subheader("分野別評価")
    st.write(f"**1. ガバナンスの整備** → {evaluate(score_1, 12)}")
    st.write(f"**2. 取引先管理** → {evaluate(score_2, 10)}")
    st.write(f"**3. リスクの特定** → {evaluate(score_3, 14)}")
    st.write(f"**4. 対策の実装** → {evaluate(score_4, 26)}")
    st.write(f"**5. 検知・監視** → {evaluate(score_5, 10)}")
    st.write(f"**6. インシデント対応** → {evaluate(score_6, 14)}")
    st.write(f"**7. 生成AI拡張チェック** → {evaluate(score_7, 6)}")

    priority_high = []
    priority_medium = []
    priority_low = []

    priority_rules = [
        ("ガバナンスの整備", score_1, 12),
        ("取引先管理", score_2, 10),
        ("リスクの特定", score_3, 14),
        ("対策の実装", score_4, 26),
        ("検知・監視", score_5, 10),
        ("インシデント対応", score_6, 14),
        ("生成AI拡張チェック", score_7, 6),
    ]

    for name, score, max_part_score in priority_rules:
        ratio = score / max_part_score
        if ratio < 0.5:
            priority_high.append(name)
        elif ratio < 0.8:
            priority_medium.append(name)
        else:
            priority_low.append(name)

    st.subheader("優先順位")
    if priority_high:
        st.error("優先度 高： " + " / ".join(priority_high))
    if priority_medium:
        st.warning("優先度 中： " + " / ".join(priority_medium))
    if priority_low:
        st.success("優先度 低： " + " / ".join(priority_low))

    st.subheader("レポート要約")
    summary_lines = []
    summary_lines.append(f"会社名：{company_name if company_name else '未入力'}")
    summary_lines.append(f"業種：{industry}")
    summary_lines.append(f"企業規模：{company_size}")
    summary_lines.append(f"入力者：{role}")
    summary_lines.append(f"SCS自己判定：{star_result}")
    summary_lines.append(f"総合スコア：{total_score} / {max_score}（達成率 {score_ratio}%）")

    if priority_high:
        summary_lines.append("優先度高の分野：" + "、".join(priority_high))
    if priority_medium:
        summary_lines.append("優先度中の分野：" + "、".join(priority_medium))
    if not priority_high and not priority_medium:
        summary_lines.append("全体として大きな不足は見られません。")

    summary_lines.append("この結果は自己診断に基づく参考値であり、正式な認証・評価を示すものではありません。")

    report_text = "\n".join(summary_lines)
    st.text_area("報告用サマリー", report_text, height=220)

    st.subheader("不足がある主な項目")
    unmet_items = []

    question_texts = {
        "q1": "法令等を踏まえた社内ルールの策定・周知",
        "q2": "責任と権限の明確化",
        "q3": "監視・分析体制",
        "q4": "守秘義務ルール",
        "q5": "セキュリティ対応方針",
        "q6": "推進計画と経営報告",
        "q7": "取引先との関係把握",
        "q8": "機密情報の取扱明確化",
        "q9": "取引先の対策状況把握",
        "q10": "インシデント時の他社との役割分担",
        "q11": "契約終了時の情報・権限回収",
        "q12": "機器・OS・ソフト情報把握",
        "q13": "ネットワーク情報把握",
        "q14": "重要情報資産の特定",
        "q15": "管理責任者の設定",
        "q16": "脅威・脆弱性・影響の把握",
        "q17": "リスク評価手順",
        "q18": "対応優先順位の決定",
        "q19": "アクセス権限設定",
        "q20": "アカウント管理ルール",
        "q21": "退職者・異動者アカウント無効化",
        "q22": "多要素認証",
        "q23": "脆弱性情報の収集",
        "q24": "パッチ適用",
        "q25": "マルウェア対策",
        "q26": "メール・ファイル感染対策",
        "q27": "ネットワーク防御",
        "q28": "外部公開システム防御",
        "q29": "異常通信検知",
        "q30": "バックアップ取得",
        "q31": "復旧確認",
        "q32": "ログ取得",
        "q33": "ログ保管",
        "q34": "ログ確認・分析",
        "q35": "監視の仕組み",
        "q36": "監視結果から初動対応への連携",
        "q37": "インシデント対応手順書",
        "q38": "連絡先一覧整備",
        "q39": "エスカレーションルール",
        "q40": "事業継続・復旧計画",
        "q41": "訓練・演習",
        "q42": "報告・公表ルール",
        "q43": "再発防止の仕組み",
        "q44": "生成AI利用ルール",
        "q45": "生成AI利用リスク整理",
        "q46": "AI for Securityの検討"
    }

    for key, value in answers.items():
        if value != "対応済み":
            unmet_items.append(f"- {question_texts[key]}（{value}）")

    if unmet_items:
        st.write(f"**不足項目数**: {len(unmet_items)} 件")
        for item in unmet_items[:15]:
            st.write(item)
        if len(unmet_items) > 15:
            st.write(f"ほか {len(unmet_items) - 15} 件あります。")
    else:
        st.write("大きな不足は確認されませんでした。")

    st.subheader("次の一手（提案）")

    if score_1 < 10:
        st.write("**ガバナンスの整備**")
        st.write("- セキュリティ方針と役割分担を文書化する")
        st.write("- 経営層への定期報告を始める")

    if score_2 < 8:
        st.write("**取引先管理**")
        st.write("- 重要取引先の洗い出しを行う")
        st.write("- 契約やチェックシートでセキュリティ要件を明確化する")

    if score_3 < 10:
        st.write("**リスクの特定**")
        st.write("- 情報資産台帳を作る")
        st.write("- リスク評価手順を定め、優先順位をつける")

    if score_4 < 20:
        st.write("**対策の実装**")
        st.write("- パッチ適用、バックアップ、アクセス制御を優先的に強化する")
        st.write("- 外部公開システムとネットワーク防御を見直す")

    if score_5 < 8:
        st.write("**検知・監視**")
        st.write("- ログ取得・保管・分析の仕組みを整える")
        st.write("- 監視結果を初動対応につなげる流れを作る")

    if score_6 < 10:
        st.write("**インシデント対応**")
        st.write("- 対応手順書、連絡先一覧、演習計画を整備する")
        st.write("- 事業継続・復旧を見据えた訓練を行う")

    if score_7 < 5:
        st.write("**生成AI拡張チェック**")
        st.write("- 生成AIの利用ルールを整備する")
        st.write("- 機密情報・個人情報・知的財産の入力可否を明文化する")
        st.write("- 生成AI利用に伴うリスクを整理する")
        st.write("- 情報収集や分析など、セキュリティ業務でのAI活用対象を洗い出す")
