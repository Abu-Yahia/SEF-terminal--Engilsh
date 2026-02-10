import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Engilsh AI Coach", page_icon="🎓")
st.title("🎓 Engilsh AI: نظام SEF المجاني")

with st.sidebar:
    st.header("🔑 إعدادات AI")
    api_key = st.text_input("أدخل مفتاح Gemini API المجاني:", type="password")

words = st.text_input("أدخل الـ 5 كلمات اليومية:")

if st.button("توليد الدرس (SEF)"):
    if not api_key:
        st.error("من فضلك ضع مفتاح الـ API المجاني في القائمة الجانبية.")
    else:
        try:
            genai.configure(api_key=api_key)
            # التحديث هنا: استخدام موديل 1.5 فلاش الأسرع والمجاني
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            prompt = f"""
            Create a SEF lesson for these words: {words}. 
            1. STUDY (S): Explanations + Past/Future sentences.
            2. EXERCISE (E): Situational questions.
            3. FOLLOW-UP (F): Emotional drama script (AJ Hoge style).
            """
            
            response = model.generate_content(prompt)
            st.markdown(response.text)
        except Exception as e:
            st.error(f"خطأ في الاتصال: {e}")
