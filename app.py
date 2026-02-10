import streamlit as st
import google.generativeai as genai

# إعدادات الصفحة
st.set_page_config(page_title="Engilsh AI Coach", page_icon="🎓")

# التنسيق الجمالي
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stButton>button { width: 100%; border-radius: 10px; background-color: #4CAF50; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎓 Engilsh: نظام SEF الذكي")
st.write("تعلم بذكاء باستخدام تقنية Gemini المجانية")

# القائمة الجانبية
with st.sidebar:
    st.header("⚙️ الإعدادات")
    api_key = st.text_input("أدخل مفتاح Gemini API المجاني:", type="password")
    st.info("احصل عليه مجاناً من Google AI Studio")

# مدخلات المستخدم
words_input = st.text_input("أدخل الـ 5 كلمات (مثال: Prefer, Avoid, Impact):")

if st.button("توليد الدرس الآن"):
    if not api_key:
        st.error("⚠️ من فضلك ضع مفتاح الـ API في القائمة الجانبية.")
    elif not words_input:
        st.warning("⚠️ الرجاء كتابة الكلمات أولاً.")
    else:
        try:
            # إعداد الذكاء الاصطناعي
            genai.configure(api_key=api_key)
            
            # محاولة استخدام الموديل الأحدث والأكثر استقراراً
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            with st.spinner('جاري تحضير محتوى SEF...'):
                prompt = f"""
                Act as a professional English coach. Create a SEF lesson for these words: {words_input}.
                Format it beautifully with headers:
                1. STUDY (S): Simple English meaning + Past and Future examples.
                2. EXERCISE (E): A situational question for each word.
                3. FOLLOW-UP (F): A short emotional drama script (AJ Hoge style) for shadowing.
                """
                
                response = model.generate_content(prompt)
                
                st.success("✅ تم توليد الدرس بنجاح!")
                st.markdown("---")
                st.markdown(response.text)
                
        except Exception as e:
            st.error(f"❌ حدث خطأ في الاتصال: {e}")

st.markdown("---")
st.caption("Engilsh Project - Version 2.0 (Stable)")
