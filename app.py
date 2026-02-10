import streamlit as st
import google.generativeai as genai

# إعدادات الصفحة
st.set_page_config(page_title="Engilsh - Free SEF Coach", page_icon="🚀")

st.title("🚀 Engilsh: نظام SEF المجاني")
st.write("تعلم بذكاء باستخدام Google Gemini (بدون تكلفة)")

# القائمة الجانبية
with st.sidebar:
    st.header("⚙️ الإعدادات المجانية")
    api_key = st.text_input("أدخل مفتاح Gemini API المجاني:", type="password")
    st.info("احصل عليه مجاناً من Google AI Studio")

words_input = st.text_input("أدخل 5 كلمات لتعلمها:")

if st.button("إنشاء الدرس مجاناً"):
    if not api_key:
        st.error("من فضلك أدخل مفتاح الـ API المجاني أولاً.")
    else:
        try:
            # إعداد نموذج جوجل
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-pro')
            
            with st.spinner('جاري بناء الدرس...'):
                prompt = f"""
                You are a professional English Coach. Create a SEF lesson for: {words_input}.
                Format:
                1. STUDY (S): Explanations + Past/Future sentences.
                2. EXERCISE (E): Situational questions.
                3. FOLLOW-UP (F): Emotional drama script (AJ Hoge style).
                """
                
                response = model.generate_content(prompt)
                st.success("تم التجهيز!")
                st.markdown(response.text)
                
        except Exception as e:
            st.error(f"حدث خطأ: {e}")
