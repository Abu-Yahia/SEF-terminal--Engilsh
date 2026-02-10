try:
    genai.configure(api_key=api_key)
    
    # محاولة استخدام الموديل الأحدث، وإذا فشل نستخدم البديل المستقر
    try:
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
    except:
        model = genai.GenerativeModel('gemini-pro')
    
    prompt = f"""
    Create a professional English lesson based on SEF (Study, Exercise, Follow-up) for these words: {words}.
    - Study (S): Simple meaning + Past/Future examples.
    - Exercise (E): One situational question for each word.
    - Follow-up (F): A short emotional drama script (AJ Hoge style).
    """
    
    response = model.generate_content(prompt)
    st.markdown(response.text)
except Exception as e:
    st.error(f"خطأ في الاتصال: {e}")
