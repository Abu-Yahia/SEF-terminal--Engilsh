import streamlit as st
import openai

# إعدادات الصفحة
st.set_page_config(page_title="Engilsh - SEF Coach", page_icon="🚀")

# التنسيق الجمالي (CSS)
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 20px; height: 3em; background-color: #007bff; color: white; }
    .stTextInput>div>div>input { border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 Engilsh: SEF Learning System")
st.write("تعلم الإنجليزية بذكاء: دراسة (S)، تدريب (E)، ومتابعة (F)")

# القائمة الجانبية للإعدادات
with st.sidebar:
    st.header("⚙️ الإعدادات")
    api_key = st.text_input("أدخل مفتاح OpenAI API:", type="password")
    st.info("هذا النظام يطبق منهجية SEF وفلسفة AJ Hoge.")

# إدخال الكلمات
words_input = st.text_input("أدخل 5 كلمات أو جمل لتعلمها اليوم (افصل بينها بفاصلة):", 
                            placeholder="مثلاً: Prefer, Avoid, Challenge, Impact, Schedule")

if st.button("ابدأ الدرس الآن"):
    if not api_key:
        st.error("من فضلك أدخل مفتاح الـ API في القائمة الجانبية أولاً.")
    elif not words_input:
        st.warning("أدخل بعض الكلمات لتبدأ!")
    else:
        try:
            client = openai.OpenAI(api_key=api_key)
            
            with st.spinner('جاري بناء درسك الاحترافي...'):
                # البرومبت المطور بناءً على تعليمات Copilot
                prompt = f"""
                You are a professional English Coach. Create a comprehensive lesson based on SEF & AJ Hoge for: {words_input}.
                Format the response beautifully using Markdown:
                
                ## 📚 PHASE 1: STUDY (S)
                Explain each word simply for an A2/B1 learner. Show each word in a 'Past' and 'Future' sentence.
                
                ## 🎯 PHASE 2: EXERCISE (E)
                Create one situational question for each word. The question must force me to use the word in my answer.
                
                ## 🎭 PHASE 3: FOLLOW-UP (F)
                Write a short, emotional 4-line drama script using all the words. 
                Include instructions on the 'Tone' (e.g., Speak angrily, Speak joyfully).
                """
                
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[{"role": "system", "content": "You are a specialized language acquisition AI."},
                              {"role": "user", "content": prompt}],
                    temperature=0.7
                )
                
                # عرض النتيجة
                st.success("تم تجهيز الدرس!")
                st.markdown("---")
                st.markdown(response.choices[0].message.content)
                
        except Exception as e:
            st.error(f"حدث خطأ فني: {e}")

# تذييل الصفحة
st.markdown("---")
st.caption("Engilsh Project - Developed by Abu-Yahia © 2026")